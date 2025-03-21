from Exception import CustomException
import sys
from src.Fever_Medicine_Recommendation.config.configuration import ModelEvaluationConfigManager
from src.Fever_Medicine_Recommendation.components.model_evaluation import ModelEvaluation

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            config = ModelEvaluationConfigManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation = ModelEvaluation(config=model_evaluation_config)
            model_evaluation.evaluation_data()
        except Exception as e:
            raise CustomException(e,sys)