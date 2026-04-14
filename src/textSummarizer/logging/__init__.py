import os, sys
import logging

logs_dir="logs"
logging_str="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"

log_filepath=os.path.join(logs_dir, "running_logs.log")
os.makedirs(logs_dir, exist_ok=True)

logging.basicConfig(
    #filename=log_filepath,
    level=logging.INFO,
    format=logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger=logging.getLogger("textSummarizerLogger")