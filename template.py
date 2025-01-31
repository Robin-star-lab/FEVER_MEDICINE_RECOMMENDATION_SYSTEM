# Template structure for the whole project
from pathlib import Path
import os
import logging

project_name = "Fever_Medicine_Recommendation"
list_of_files = [
    "main.py",
    "requirements.txt",
    "app.py",
    "setup.py",
    "src/__init__.py",
    "src/Resources/trials.ipynb",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/entities.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "schema.yaml"
]


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s: %(levelname)s: %(module)s: %(message)s]",
    datefmt="%d-%m-%Y %H:%M:%S"
)
for filepath in list_of_files:
    filepath = Path(filepath)
    file_dir,filename = os.path.split(filepath)
    if file_dir != "":
        os.makedirs(file_dir,exist_ok=True)
        logging.info(f"Creating directory: {file_dir} for the file {filename}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as F:
            pass
        logging.info(f"Creating empty file: {filepath}")
        