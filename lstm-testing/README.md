## Summary

This folder contains runnable notebooks that test Long Short-Term Memory (LSTM) neural network models on some of our sustainability data. 

`**test_lstm.ipynb`:** A more simple LSTM model using numerical simulated data to predict CO2 emissions.
**`emission_reduction_lstm`::** A multivariate LSTM model using one-hot encoded variables from provided ImpactEdge database data to predict stationary combustion activity.

The individual notebooks can be ran through step by step. Note that the grid search procedure to select the best performing model may take considerable time and processing, especially in the case of the `emission_reduction_lstm` file.

## Requirements

The requirements to run these files successfully are:
 - Python (3.x)
 - pip or equivalent
 - Installing the required dependencies as below:

```bash
cd lstm-testing
pip install -r requirements.txt
```

 - Also make sure to modify the `database.env` with your database details before running the `emission_reduction_lstm` notebook. `DB_NAME` refers to the database's name, `DB_USER` and `DB_PASS` refer to username and password, `HOST` and `PORT` are self-explanatory.