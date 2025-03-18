from src.Fever_Medicine_Recommendation.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from logger import fever_logger
from Exception import CustomException
import sys
Stage = 'Data Ingestion Stage'

if __name__ == '__main__':
    try:
        pipeline = DataIngestionPipeline()
        pipeline.main()
        fever_logger.info(f"{Stage} Completed successfully")
    except Exception as e:
        raise CustomException(e,sys)