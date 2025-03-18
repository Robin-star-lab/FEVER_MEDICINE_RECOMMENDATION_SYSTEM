from logger import fever_logger
import zipfile
import pandas as pd
from urllib.error import HTTPError
import urllib.request as request
from src.Fever_Medicine_Recommendation.entity.entities import DataIngestionConfig
import os


class DataIngestion():
    def __init__(self, config:DataIngestionConfig):
        self.config = config
    
    def load_data(self):
        # This function loads data from github
        local_data_path = self.config.data_dir
        if (not os.path.exists(local_data_path)):
            file_name,headers = request.urlretrieve(
                url=self.config.source_url,
                filename=local_data_path
            )
            fever_logger.info(f"Data downloaded from: {self.config.source_url} into: {local_data_path}")
    def extract_data(self):
        # This function extracts data from the downloaded zipfile
        local_data_path = self.config.data_dir
        unzip_data = self.config.unzipped_data
        if unzip_data !="":
            os.makedirs(unzip_data,exist_ok=True)
        else:
            fever_logger.info("Folder already exists")
        with zipfile.ZipFile(local_data_path) as zipref:
            zipref.extractall(unzip_data)
            
        fever_logger.info(f"Extracted the zipfile: {local_data_path} into: {unzip_data}")
        
    
        
    