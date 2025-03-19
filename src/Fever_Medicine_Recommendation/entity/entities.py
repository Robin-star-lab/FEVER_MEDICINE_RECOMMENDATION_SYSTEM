from dataclasses import dataclass
from pathlib import Path


@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    data_dir: Path
    unzipped_data: Path
    

@dataclass
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    train_data_path: Path
    test_data_path: Path
    preprocessor_path: Path
    
    