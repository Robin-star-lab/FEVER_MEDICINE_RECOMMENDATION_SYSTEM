from src.Fever_Medicine_Recommendation.utils.common import load_preprocessor,load_model
from pathlib import Path
from Exception import CustomException
import sys
import pandas as pd



class Prediction:
    def __init__(self, preprocessor,model):
        self.preprocessor = load_preprocessor(Path("artifacts\data_transformation\preprocessor.pkl"))
        self.model = load_model(Path("artifacts\model_training\model.regressor"))
        
    def predict(self, patients_data):
        # Preprocess the input data
        preprocessed_data = self.preprocessor.transform(patients_data)
        prediction = self.model.predict(preprocessed_data)
        
        return prediction
    

class CustomData:
    def __init__(self,
                 Temperature: float,
                 Fever_Severity: str,
                 Age: int,
                 Gender: str,
                 BMI: float,
                 Headache: str,
                 Body_Ache: str,
                 Fatigue: str,
                 Chronic_Conditions: str,
                 Allergies: str,
                 Smoking_History: str,
                 Alcohol_Consumption: str,
                 Humidity: float,
                 AQI: int,
                 Physical_Activity: str,
                 Diet_Type: str,
                 Heart_rate: int,
                 Blood_Pressure: str,
                 Previous_Medication: str):
        self.Temperature = Temperature
        self.Fever_Severity = Fever_Severity
        self.Age = Age
        self.Gender = Gender
        self.BMI = BMI
        self.Headache = Headache
        self.Body_Ache = Body_Ache
        self.Fatigue = Fatigue
        self.Chronic_Conditions = Chronic_Conditions
        self.Allergies = Allergies
        self.Smoking_History = Smoking_History
        self.Alcohol_Consumption = Alcohol_Consumption
        self.Humidity = Humidity
        self.AQI = AQI
        self.Physical_Activity = Physical_Activity
        self.Diet_Type = Diet_Type
        self.Heart_rate = Heart_rate
        self.Blood_Pressure = Blood_Pressure
        self.Previous_Medication = Previous_Medication
        
    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                "Temperature": [self.Temperature],
                "Fever_Severity": [self.Fever_Severity],
                "Age": [self.Age],
                "Gender": [self.Gender],
                "BMI": [self.BMI],
                "Headache": [self.Headache],
                "Body_Ache": [self.Body_Ache],
                "Fatigue": [self.Fatigue],
                "Chronic_Conditions": [self.Chronic_Conditions],
                "Allergies": [self.Allergies],
                "Smoking_History": [self.Smoking_History],
                "Alcohol_Consumption": [self.Alcohol_Consumption],
                "Humidity": [self.Humidity],
                "AQI": [self.AQI],
                "Physical_Activity": [self.Physical_Activity],
                "Diet_Type": [self.Diet_Type],
                "Heart_rate": [self.Heart_rate],
                "Blood_Pressure": [self.Blood_Pressure],
                "Previous_Medication": [self.Previous_Medication]
            }
        except Exception as e:
            raise CustomException(e,sys)
        
        input_dataframe = pd.DataFrame(custom_data_input_dict)
        return input_dataframe