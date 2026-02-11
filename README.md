This repository will show the results of various methods to predict sustainability data and track anomalies present in the data.

 - **`lstm_testing`** shows the results of using an LSTM (Long Short-Term Memory) model to predict stationary combustion (Scope 1) data.
 - **`isolation-forest-detection`** detects anomalies in stationary combustion (Scope 1) data using an Isolated Forest model and assigns them "anomaly scores" depending on how likely they are to actually be anomalies.

## Requirements

The requirements to run these files successfully are:
 - Python (3.x)
 - pip or equivalent
 - Installing the required dependencies as below:

```bash
cd lstm-testing
pip install -r requirements.txt
```

