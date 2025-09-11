# generate_data.py
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def generate_vitals_dataset(num_records=10000, output_file='patient_vitals_dataset.csv'):
    """
    Generate a synthetic dataset of patient vitals for training the triage model
    """
    print(f"Generating {num_records} synthetic patient records...")
    
    # Define normal ranges for vital signs
    vital_ranges = {
        'heart_rate': (60, 100),  # bpm
        'blood_pressure_systolic': (90, 120),  # mmHg
        'blood_pressure_diastolic': (60, 80),  # mmHg
        'temperature': (36.1, 37.2),  # Celsius
        'oxygen_saturation': (95, 100),  # percentage
        'respiratory_rate': (12, 20)  # breaths per minute
    }
    
    # Create empty lists to store data
    data = {
        'patient_id': [],
        'heart_rate': [],
        'blood_pressure_systolic': [],
        'blood_pressure_diastolic': [],
        'temperature': [],
        'oxygen_saturation': [],
        'respiratory_rate': [],
        'recorded_at': [],
        'urgency_level': []
    }
    
    # Generate patient IDs
    patient_ids = list(range(1, 2001))  # 2000 unique patients
    
    # Generate records
    for i in range(num_records):
        # Randomly select a patient
        patient_id = random.choice(patient_ids)
        data['patient_id'].append(patient_id)
        
        # Generate timestamp within the last 30 days
        days_ago = random.randint(0, 30)
        timestamp = datetime.now() - timedelta(days=days_ago, 
                                              hours=random.randint(0, 23),
                                              minutes=random.randint(0, 59))
        data['recorded_at'].append(timestamp.strftime('%Y-%m-%d %H:%M:%S'))
        
        # Decide if this is an emergency case (20% of cases)
        is_emergency = random.random() < 0.2
        
        # Generate vital signs based on whether this is an emergency
        for vital, (min_val, max_val) in vital_ranges.items():
            if is_emergency:
                # For emergency cases, generate more extreme values
                deviation = random.choice([-1, 1]) * random.uniform(0.2, 0.5)
                if deviation > 0:
                    # Value above normal range
                    value = max_val + (max_val - min_val) * deviation
                else:
                    # Value below normal range
                    value = min_val + (max_val - min_val) * deviation
            else:
                # For non-emergency cases, generate values within normal range
                # with occasional slight deviations
                deviation = random.uniform(-0.1, 0.1)
                value = min_val + (max_val - min_val) * (0.5 + deviation)
            
            # Add some random noise
            noise = random.uniform(-0.05, 0.05) * (max_val - min_val)
            value += noise
            
            # Round to appropriate precision
            if vital == 'temperature':
                value = round(value, 1)
            else:
                value = round(value)
            
            data[vital].append(value)
        
        # Set urgency level based on vitals
        if is_emergency:
            # For obvious emergencies
            urgency = random.choice(['emergency', 'urgent'])
        else:
            # For non-emergencies
            urgency = random.choice(['standard', 'non-urgent'])
            
        data['urgency_level'].append(urgency)
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Save to CSV
    df.to_csv(output_file, index=False)
    print(f"Dataset generated and saved to {output_file}")
    
    # Return the DataFrame
    return df

if __name__ == "__main__":
    generate_vitals_dataset(10000)