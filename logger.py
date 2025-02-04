import logging
import os
import sys

log_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
log_dir = "logs"
if log_dir != "":
    os.makedirs(log_dir,exist_ok=True)
    
    log_file_path = os.path.join(log_dir,"running_logs.log")

logging.basicConfig(
    level=logging.INFO,
    format=log_str,
    handlers=[
        logging.FileHandler(log_file_path),
        logging.StreamHandler(sys.stdout)
    ]
)
fever_logger = logging.getLogger("fever_logger")