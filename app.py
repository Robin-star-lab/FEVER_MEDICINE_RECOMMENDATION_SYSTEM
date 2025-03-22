from flask import Flask,render_template,request
from Exception import CustomException
import sys
import numpy as np
import pandas as pd
from src.Fever_Medicine_Recommendation.pipeline.prediction_pipeline import Prediction,CustomData

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')
@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        try:
            # Reading inputsgiven by the user
            data = CustomData(
                Temperature = float(request.form.get('Temperature')),
                Fever_Severity = str(request.form.get('Fever_Severity')),
                Age= int(request.form.get('Age')),
                Gender = bool(request.form.get('Gender')),
                BMI = float(request.form.get('BMI')),
                Headache = str(request.form.get('Headache')),
                Body_Ache = str(request.form.get('Body_Ache')),
                Fatigue = str(request.form.get('Fatigue')),
                Chronic_Conditions = str(request.form.get('Chronic_Conditions')),
                Allergies = str(request.form.get('Allergies')),
                Smoking_History = str(request.form.get('Smoking_History')),
                Alcohol_Consumption = str(request.form.get('Alcohol_Consumption')),
                Humidity = float(request.form.get('Humidity')),
                AQI = int(request.form.get('AQI')),
                Physical_Activity = str(request.form.get('Physical_Activity')),
                Diet_Type = str(request.form.get('Diet_Type')),
                Heart_rate = int(request.form.get('Heart_rate')),
                Blood_Pressure = str(request.form.get('Blood_Pressure')),
                Previous_Medication = str(request.form.get('Previous_Medication'))
            )
            
            
            final_data = data.get_data_as_dataframe()
            prediction = Prediction()
            my_predictions = prediction.predict(final_data)
            

            if isinstance(my_predictions, np.ndarray):
                # Check if it's a NumPy array
                if my_predictions.size == 1:
                    # Check if it has only one element
                     prediction_value = my_predictions.item()  # Extract the value
                else:
                    
                # Handle the case where there are multiple predictions
                # For example, take the first one:
                    prediction_value = my_predictions.flat[0]
            # Or choose another appropriate strategy
            else:
                # If it's not a NumPy array, try to get the first element
                try:
                    
                    prediction_value = my_predictions[0] 
                except (TypeError, IndexError):
                    # Handle potential errors
                    prediction_value = my_predictions # If it's already a single value

                    # Convert to integer AFTER extracting the single value
                    prediction_value = int(prediction_value) 

            return render_template('results.html', my_predictions=prediction_value)
            
        except Exception as e:
            raise CustomException(e,sys)
            

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True, port = 8080)