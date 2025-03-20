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
    

@dataclass
class ModelTrainerConfig:
    root_dir: Path
    model_path: Path
    train_data_path: Path
    metrics_path: Path
    penalty: str
    solver: str
    multiclass: str
    fit_intercept: bool
    max_iter: int
    C: float