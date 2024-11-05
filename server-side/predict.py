import sys
import json
import numpy as np
import pandas as pd
import joblib


model = joblib.load('./model/xgboost_model.pkl')
scaler = joblib.load('./model/scaler.pkl')


feature_names = ['Temperature', 'DHI', 'DNI', 'GHI', 'Hour_Sin', 'Hour_Cos', 'Month_Sin', 'Month_Cos']

def predict(features):
    
    
    feature_list = [[
        feature["Temperature"],
        feature["DHI"],
        feature["DNI"],
        feature["GHI"],
        feature["Hour_Sin"],
        feature["Hour_Cos"],
        feature["Month_Sin"],
        feature["Month_Cos"]
    ] for feature in features]

    features_df = pd.DataFrame(feature_list, columns=feature_names)

    # Scale the features using the loaded scaler
    features_scaled = scaler.transform(features_df)

    # Predict using the loaded XGBoost model
    predictions = model.predict(features_scaled)
    
    return predictions.tolist()


if __name__ == "__main__":
    input_data = sys.stdin.read()
    print("Received input:", input_data, file=sys.stderr)  # Debug print
    features = json.loads(input_data)
    print("Parsed features:", features, file=sys.stderr)  # Debug print
    results = predict(features)
    print("Predictions:", results, file=sys.stderr)  # Debug print
    import json
    print(json.dumps(results))
