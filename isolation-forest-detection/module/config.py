import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='database.env')

# Database Config
DB_CONFIG = {
    "dbname": os.environ.get('DB_NAME'),
    "user": os.environ.get('DB_USER'),
    "password": os.environ.get('DB_PASS'),
    "host": os.environ.get('HOST'),
    "port": os.environ.get('PORT')
}

# IMPORTANT: The first column should be a timestamp for when data was uploaded.
TABLE_QUERY = 'SELECT "createdAt","facilityId","co2e","fuelHint","ch4","n2o","ef","co2" FROM stationary_combustion_activity'

# Model Hyperparameters
MODEL_PARAMS = {
    "estimators": 100,
    "contamination": 'auto',
    "window_size": '180D',
    "contamination_rate": 0.01,
    "random_state": 42
}

# Feature definitions
NUMERICAL_FEATURES = ['co2e', 'ch4', 'n2o', 'ef', 'co2', 'month_sin', 'month_cos']
CATEGORICAL_FEATURES = ['facilityId', 'fuelHint']