import pandas as pd
import numpy as np
import psycopg2
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import IsolationForest
import config

class AnomalyDetector:
    def __init__(self):
        self.model_pipeline = self._build_pipeline()
        self.window_size = config.MODEL_PARAMS["window_size"]
        self.contamination_rate = config.MODEL_PARAMS["contamination_rate"]

    def _build_pipeline(self):
        """Creates the preprocessing and model pipeline."""
        numerical_transformer = StandardScaler()
        categorical_transformer = OneHotEncoder(handle_unknown='ignore', sparse_output=False)

        preprocessor = ColumnTransformer(
            transformers=[
                ('num', numerical_transformer, config.NUMERICAL_FEATURES),
                ('cat', categorical_transformer, config.CATEGORICAL_FEATURES)
            ]
        )

        return Pipeline(steps=[
            ('preprocessor', preprocessor),
            ('model', IsolationForest(
                n_estimators=config.MODEL_PARAMS["estimators"],
                contamination=config.MODEL_PARAMS["contamination"],
                random_state=config.MODEL_PARAMS["random_state"],
                n_jobs=-1
            ))
        ])

    def fetch_data(self):
        """Connects to DB and returns a dataframe."""
        conn = psycopg2.connect(**config.DB_CONFIG)
        query = config.TABLE_QUERY
        df = pd.read_sql(query, conn)
        conn.close()
        return df

    def engineer_features(self, df):
        """Standardizes data cleaning steps."""
        df[df.columns[0]] = pd.to_datetime(df[df.columns[0]], utc=True)
        df['month'] = df[df.columns[0]].dt.month
        df['month_sin'] = np.sin(2 * np.pi * df['month']/12)
        df['month_cos'] = np.cos(2 * np.pi * df['month']/12)
        
        return df

    def run_detection(self, df):
        """Fits the model and applies dynamic rolling thresholds."""
        features = config.NUMERICAL_FEATURES + config.CATEGORICAL_FEATURES
        X = df[features]

        # Fit and get raw scores
        self.model_pipeline.fit(X)
        df['anomaly_score'] = self.model_pipeline.decision_function(X)

        # Sort for rolling calculations
        df = df.sort_values('createdAt').set_index('createdAt')

        # Calculate Dynamic Threshold
        df['rolling_threshold'] = (
            df['anomaly_score']
            .rolling(window=self.window_size, closed='left')
            .quantile(self.contamination_rate)
        )

        # Fallback for cold-start
        static_fallback = df['anomaly_score'].quantile(self.contamination_rate)
        df['rolling_threshold'] = df['rolling_threshold'].fillna(static_fallback)

        # Labeling
        df['is_anomaly'] = np.where(df['anomaly_score'] < df['rolling_threshold'], -1, 1)

        return df.reset_index()