import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='data/database.env')

# Choice of: 'db', 'csv', or 'json'
# For loading from a database, .csv file, or .json file respectively.
DATA_SOURCE = 'db' 

# Database Config
DB_CONFIG = {
    "dbname": os.environ.get('DB_NAME'),
    "user": os.environ.get('DB_USER'),
    "password": os.environ.get('DB_PASS'),
    "host": os.environ.get('HOST'),
    "port": os.environ.get('PORT')
}

# File path for CSV file
CSV_PATH = 'data/combustion_data.csv'

# File path for JSON file
# Use JSON_ORIENT='records' or 'split' depending on how your JSON is structured
JSON_PATH = 'data/combustion_data.json'
JSON_ORIENT = 'records'

# IMPORTANT: The first column should be a timestamp for when data was uploaded.
TABLE_QUERY = 'SELECT "createdAt","facilityId","co2e","fuelHint","ch4","n2o","ef","co2" FROM purchased_electricity_activity'

# Model Hyperparameters
MODEL_PARAMS = {
    "estimators": 100, # number of isolation trees we use for our model
    "contamination": 'auto', # expected ratio of outliers for model, leave as "auto" if you don't want the model to make assumptions
    "window_size": '180D', # size of our rolling time window for defining outliers under
    "contamination_rate": 0.01, # expected ratio of outliers in rolling window
    "random_state": 42 # random seed to replicate output, set to whatever you wish
}

# Feature definitions
NUMERICAL_FEATURES = ['co2e', 'ch4', 'n2o', 'ef', 'co2']
CATEGORICAL_FEATURES = ['facilityId', 'fuelHint']

# Name of output file
OUTPUT_FILE = "output/detected_anomalies.csv"