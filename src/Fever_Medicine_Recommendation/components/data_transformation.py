from src.Fever_Medicine_Recommendation.constants import *
from src.Fever_Medicine_Recommendation.utils.common import read_yaml,create_directories,save_preprocessor
from sklearn.model_selection import  train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OrdinalEncoder, StandardScaler,OneHotEncoder
from sklearn.pipeline import Pipeline
from imblearn.over_sampling import SMOTE
from sklearn.impute import SimpleImputer
from src.Fever_Medicine_Recommendation.entity.entities import DataTransformationConfig
import pandas as pd
import os
import numpy as np




class DataTransformation:
    def __init__(self, config:DataTransformationConfig):
        self.config = config
    def acquire_data(self):
        data_path = self.config.data_path
        self.data = pd.read_csv(Path(data_path))
    def initiate_data_transformstion(self):
        data = self.data
        data['Recommended_Medication'] = data['Recommended_Medication'].replace({'Ibuprofen': 1,'Paracetamol': 2})
        X_variables = data.drop(columns='Recommended_Medication')
        Y_variable = data['Recommended_Medication']
        
        self.X_train, self.X_test, self.Y_train, self.Y_test = train_test_split(X_variables,Y_variable,test_size=0.3,random_state=42)
        self.numerical_features = X_variables.select_dtypes(exclude='object').columns
        self.categorical_features = X_variables.select_dtypes(include='object').columns
        
    
    def data_processing(self):
        numerical_columns = self.numerical_features
        categorical_columns = self.categorical_features
        
            # Separate ordinal and nominal (unordered) categorical features
        ordinal_features = ['Fever_Severity', 'Physical_Activity', 'Blood_Pressure']
        nominal_features = [col for col in categorical_columns if col not in ordinal_features]
        
        # Create mappings for ordinal features
        ordinal_mappings = {
            'Fever_Severity': ['High Fever', 'Mild Fever', 'Normal'],
            'Physical_Activity': ['Active', 'Moderate', 'Sedentary'],
            'Blood_Pressure': ['High', 'Normal', 'Low']
            }
        #  Create the list of category orders for ordinal features
        ordinal_categories = [ordinal_mappings[col] for col in ordinal_features if col in categorical_columns]
        
            # Define transformers
        numerical_transformer = Pipeline(
            steps=[
            ('scaler', StandardScaler())
            ])
        # Transformer for ordinal categorical features
        ordinal_transformer = Pipeline(
            steps=[
            ('impute', SimpleImputer(strategy='most_frequent')),
            ('ordinal', OrdinalEncoder(categories=ordinal_categories))
            ])
        # Transformer for nominal (unordered) categorical features
        nominal_transformer = Pipeline(
            steps=[
            ('impute', SimpleImputer(strategy='most_frequent')),
            ('onehot', OneHotEncoder(handle_unknown='ignore'))
            ])
            # Create a column transformer with all three types
        preprocessor = ColumnTransformer(
            transformers=[
            ('numerical', numerical_transformer, numerical_columns),
            ('ordinal', ordinal_transformer, [col for col in ordinal_features if col in categorical_columns]),
            ('nominal', nominal_transformer, nominal_features)
            ])
        os.makedirs(self.config.preprocessor_path, exist_ok=True)
    
        preprocessor.fit(self.X_train)
    
        
        from pathlib import Path


        save_preprocessor(Path(os.path.join(self.config.preprocessor_path, 'preprocessor.pkl')), preprocessor)

    
    
        x_train_transformed = preprocessor.transform(self.X_train)
    
        smote = SMOTE(sampling_strategy='auto')
        x_train_balanced, y_train_balanced = smote.fit_resample(x_train_transformed, self.Y_train)
        x_test_transformed = preprocessor.transform(self.X_test)
    
    
        scaled_train_df = pd.DataFrame(x_train_balanced, columns=preprocessor.get_feature_names_out())
        scaled_test_df = pd.DataFrame(x_test_transformed, columns=preprocessor.get_feature_names_out())
    
        scaled_train_array = np.c_[scaled_train_df, np.array(y_train_balanced)]
        scaled_test_array = np.c_[scaled_test_df, np.array(self.Y_test)]
    
        # Add column names to the final dataframes
        feature_names = list(preprocessor.get_feature_names_out())
        column_names = feature_names + ['Recommended_Medication']
    
        scaled_train = pd.DataFrame(scaled_train_array, columns=column_names)
        scaled_test = pd.DataFrame(scaled_test_array, columns=column_names)
    
        scaled_train.to_csv(os.path.join(self.config.train_data_path, 'train_data.csv'), index=False)
        scaled_test.to_csv(os.path.join(self.config.test_data_path, 'test_data.csv'), index=False)

    
    
        
        
        
        
        
        