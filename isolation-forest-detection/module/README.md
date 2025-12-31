## Data Entry Instructions

If you are using a `.csv` or `.json` file, upload it to the `data` folder. If you are using a table from a database, modify the `database.env` file appropriately. Then modify the `config.py` variables accordingly based on the instructions provided.

## Requirements

The requirements to run these files successfully are:
 - Python (3.x)
 - pip or equivalent
 - Installing the required dependencies as below:

```bash
cd isolation-forest-detection/module
pip install -r requirements.txt
```

## Running the Module

Run the `main.py` file. If everything works, it should upload a list of anomalies as a file with the type and name you provided in `config.py`.