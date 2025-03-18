from src.Fever_Medicine_Recommendation.constants import *
from src.Fever_Medicine_Recommendation.utils.common import read_yaml,create_directories
from src.Fever_Medicine_Recommendation.entity.entities import DataIngestionConfig


class DataIngestionConfigManager:
    def __init__(self, config_file_path = CONFIG_FILE_PATH):
        self.config = read_yaml(config_file_path)
        
        create_directories([self.config.Artifacts_root])
    
    def data_ingestion_config(self)->DataIngestionConfig:
        config = self.config.data_ingestion
        
        create_directories([config.root_dir])
        
        get_data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_url = config.source_url,
            data_dir = config.data_dir,
            unzipped_data = config.unzipped_data
            
        )
        return get_data_ingestion_config