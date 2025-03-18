from src.Fever_Medicine_Recommendation.config.configuration import DataIngestionConfigManager
from src.Fever_Medicine_Recommendation.components.data_ingestion import DataIngestion


class DataIngestionPipeline():
    def __init__(self):
        pass
    def main(self):
        config = DataIngestionConfigManager()
        data_ingestion_config = config.data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.load_data()
        data_ingestion.extract_data()
        
        