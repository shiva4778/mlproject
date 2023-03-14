import logging
from datetime import datetime
import os

LOG_DIRS = "Student_log"
LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs", LOG_DIRS)
try:
    os.makedirs(logs_path, exist_ok=True)
except OSError as e:
    print(f"Error creating directory {logs_path}: {e}")
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)
logging.basicConfig(level=logging.INFO, filename=LOG_FILE_PATH, filemode='w', format='[%(asctime)s] %(name)s %(levelname)s %(message)s')
