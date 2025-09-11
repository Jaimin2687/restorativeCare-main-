# predict.py
import joblib
import json
import sys
from patient_triage import predict_patient_urgency, FEATURES, MODEL_FILENAME

def main():
    print("Patient Triage Prediction")
    print("========================")
    
    # Load the model
    try:
        model = joblib.load(MODEL_FILENAME)
        print(f"Model loaded from {MODEL_FILENAME}")
    except:
        print(f"Error: Model file {MODEL_FILENAME} not found. Please train the model first.")
        return
    
    # Get user input for vitals
    vitals = {}
    print("\nPlease enter the patient's vital signs:")
    
    for feature in FEATURES:
        while True:
            try:
                value = float(input(f"{feature.replace('_', ' ').title()}: "))
                vitals[feature] = value
                break
            except ValueError:
                print("Please enter a valid number.")
    
    # Make prediction
    try:
        result = predict_patient_urgency(vitals, model)
        
        print("\nPrediction Result:")
        print(f"Emergency Status: {'EMERGENCY' if result['is_emergency'] else 'NON-EMERGENCY'}")
        print(f"Confidence: {result['confidence'] * 100:.1f}%")
        print(f"Recommendation: {result['recommendation']}")
        print(f"Probability of Emergency: {result['probability_emergency'] * 100:.1f}%")
    except Exception as e:
        print(f"Error making prediction: {str(e)}")
    
if __name__ == "__main__":
    main()