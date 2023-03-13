import logging
from datetime import datetime
import os

LOG_DIRS='Housing_log'
CURRENT_TIME_STAMP=f"{datetime.now().strftime('%Y-%m-%D:%H-%M-%S')}"
os.makedirs(LOG_DIRS,exist_ok=True)
log_file_name=f"log-{CURRENT_TIME_STAMP}.log"
log_file_path=os.path.join(LOG_DIRS,log_file_name)
logging.basicConfig(level=logging.INFO,filename=log_file_path,filemode='w',format='[%(asctime)s]%(name)s%(levelname)s-%(message)s')
