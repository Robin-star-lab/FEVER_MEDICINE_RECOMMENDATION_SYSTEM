from Exception import CustomException
from src.Fever_Medicine_Recommendation.config.configuration import DataTransformationConfigManager
from src.Fever_Medicine_Recommendation.components.data_transformation import DataTransformation
import sys


class DataTransformationPipeline:
    def __init__(self):
        pass
    def main(self):
        try:
            config = DataTransformationConfigManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(config=data_transformation_config)
            data_transformation.acquire_data()
            data_transformation.initiate_data_transformstion()
            data_transformation.data_processing()
            
        except Exception as e:
            raise CustomException(e,sys)