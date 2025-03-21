
from src.Fever_Medicine_Recommendation.entity.entities import  ModelEvaluationConfig
import pandas as pd
from Exception import CustomException
import sys
from pathlib import Path
from sklearn.metrics import confusion_matrix, precision_score, recall_score
from src.Fever_Medicine_Recommendation.utils.common import load_model,save_metrics
import os

class ModelEvaluation:
    def __init__(self, config:ModelEvaluationConfig):
        self.config = config
    
    def evaluation_data(self):
        data = self.config.test_data_path
        test_data = pd.read_csv(Path(data))
        X_test = test_data.drop('Recommended_Medication', axis=1)
        Y_test = test_data['Recommended_Medication']
        
        model = load_model(Path(self.config.model_path))
        y_pred = model.predict(X_test)
        actual = Y_test
        confusion = confusion_matrix(actual, y_pred)
        precision = precision_score(actual, y_pred)
        recall = recall_score(actual, y_pred)
        
        save_metrics(Path(os.path.join(self.config.metrics_path,'confusion.metrics')),confusion)
        save_metrics(Path(os.path.join(self.config.metrics_path,'precision.metrics')),precision)
        save_metrics(Path(os.path.join(self.config.metrics_path,'recall.metrics')),recall)
        
        