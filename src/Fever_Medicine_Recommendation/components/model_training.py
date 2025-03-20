import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from dataclasses import dataclass
import sys
from pathlib import Path
from Exception import CustomException
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd
from src.Fever_Medicine_Recommendation.entity.entities import ModelTrainerConfig
import os
from sklearn.metrics import confusion_matrix
from src.Fever_Medicine_Recommendation.utils.common import save_model




class ModelTraining:
    def __init__(self, config:ModelTrainerConfig):
        self.config =config
        
    def initiate_model_training(self):
        training_data = self.config.train_data_path
        data = pd.read_csv(Path(training_data))
        X_train = data.drop('Recommended_Medication',axis=1)
        Y_train = data['Recommended_Medication']
        # Split the data into training and testin sets
        x_train,x_test,y_train,y_test = train_test_split(X_train,Y_train,test_size=0.3,random_state=42)
        logistic_regressor = LogisticRegression(penalty=self.config.penalty,
                                                solver=self.config.solver,
                                                max_iter=self.config.max_iter,
                                                C=self.config.C,
                                                multi_class=self.config.multiclass,
                                                fit_intercept=self.config.fit_intercept
                                                )
        model = logistic_regressor.fit(x_train,y_train)
        self.model_name = 'model.regressor'
        save_model(Path(os.path.join(self.config.model_path,self.model_name)),model)
        self.y_pred = model.predict(x_test)
        self.actual = y_test
        self.metrics = confusion_matrix(self.y_pred,self.actual)
    def save_confusion_matrix(self):
        
    
        
        try:
            
            # Create directory if it doesn't exist
            os.makedirs(self.config.metrics_path, exist_ok=True)
        
            # Calculate confusion matrix
            cm = self.metrics
        
            # Save as CSV
            cm_df = pd.DataFrame(
                
                cm, 
                index=[f'True_{i}' for i in np.unique(self.actual)],
                columns=[f'Pred_{i}' for i in np.unique(self.actual)]
                )
            cm_df.to_csv(os.path.join(self.config.metrics_path, f"{self.model_name}_confusion_matrix.csv"))
        
            # Create visualization
            plt.figure(figsize=(10, 8))
            sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                    xticklabels=np.unique(self.actual),
                    yticklabels=np.unique(self.actual))
            plt.xlabel('Predicted')
            plt.ylabel('True')
            plt.title(f'Confusion Matrix - {self.model_name}')
        
            # Save plot
            plt.savefig(os.path.join(self.config.metrics_path, f"{self.model_name}_confusion_matrix.png"), dpi=300, bbox_inches='tight')
            plt.close()
        
            print(f"Confusion matrix saved to {self.config.metrics_path}")
        
        except Exception as e:
            
            print(f"Error saving confusion matrix: {str(e)}")
