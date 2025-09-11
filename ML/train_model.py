# train_model.py
import sys
import os
from patient_triage import load_data, preprocess_data, train_model
from generate_data import generate_vitals_dataset

def main():
    print("Patient Triage Model Training")
    print("============================")
    
    # Check if dataset exists, generate if not
    dataset_path = 'patient_vitals_dataset.csv'
    if not os.path.exists(dataset_path):
        print(f"Dataset not found at {dataset_path}")
        print("Generating synthetic dataset...")
        generate_vitals_dataset(10000, dataset_path)
    
    # Load data
    df = load_data(dataset_path)
    
    # Preprocess data
    processed_df = preprocess_data(df)
    
    # Train model
    model = train_model(processed_df)
    
    print("\nTraining complete! The model is ready for use.")
    
if __name__ == "__main__":
    main()