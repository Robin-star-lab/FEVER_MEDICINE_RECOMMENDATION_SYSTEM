from src.Fever_Medicine_Recommendation.components.model_training import ModelTraining
from src.Fever_Medicine_Recommendation.config.configuration import ModelTrainerConfigManager
import sys
from Exception import CustomException


class ModelTrainerPipeline:
    def __init__(self):
        pass
    def main(self):
        try:
            config = ModelTrainerConfigManager()
            training_config = config.get_model_trainer_config()
            model_trainer = ModelTraining(config=training_config)
            model_trainer.initiate_model_training()
            model_trainer.save_confusion_matrix()
        except Exception as e:
            raise CustomException(e,sys)