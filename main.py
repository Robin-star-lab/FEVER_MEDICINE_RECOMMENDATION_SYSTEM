from src.Fever_Medicine_Recommendation.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from logger import fever_logger
from src.Fever_Medicine_Recommendation.pipeline.data_transformation_pipeline import DataTransformationPipeline
from Exception import CustomException
from src.Fever_Medicine_Recommendation.pipeline.model_training_pipeline import ModelTrainerPipeline
from src.Fever_Medicine_Recommendation.pipeline.model_eval_pipeline import ModelEvaluationPipeline
import sys
Stage = 'Data Ingestion Stage'

if __name__ == '__main__':
    try:
        pipeline = DataIngestionPipeline()
        pipeline.main()
        fever_logger.info(f"********************{Stage}******************** Completed successfully")
    except Exception as e:
        raise CustomException(e,sys)
    
    
Stage = 'Data Transformation Stage'

if __name__ == '__main__':
    try:
        pipeline = DataTransformationPipeline()
        pipeline.main()
        fever_logger.info(f"********************{Stage}******************* Completed successfully")
    except Exception as e:
        raise CustomException(e,sys)
    
    
Stage = 'Model Training Stage'

if __name__ == '__main__':
    try:
        pipeline = ModelTrainerPipeline()
        pipeline.main()
        fever_logger.info(f"********************{Stage}******************* Completed successfully")
    except Exception as e:
        raise CustomException(e,sys)
    
    
Stage = 'Model Evaluation Stage'

if __name__ == "__main__":
    try:
        pipeline = ModelEvaluationPipeline()
        pipeline.main()
        fever_logger.info(f"********************{Stage}******************* Completed successfully")
    except Exception as e:
        raise CustomException(e,sys)