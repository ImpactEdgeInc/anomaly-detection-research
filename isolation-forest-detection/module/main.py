from anomaly_detect import AnomalyDetector
import config

def main():
    detector = AnomalyDetector()
    
    print("Fetching data...")
    raw_data = detector.fetch_data()
    
    print("Engineering features...")
    processed_data = detector.engineer_features(raw_data)
    
    print("Running Anomaly Detection...")
    results = detector.run_detection(processed_data)
    
    anomalies = results[results['is_anomaly'] == -1]
    anomalies = anomalies.drop('is_anomaly', axis=1)
    print(f"Detection complete. Total anomalies found: {len(anomalies)}")
    
    # Export or alert
    anomalies.to_csv(config.OUTPUT_FILE, index=False)
    print("Results saved to detected_anomalies.csv")

if __name__ == "__main__":
    main()