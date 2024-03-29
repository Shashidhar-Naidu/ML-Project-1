import logging
import os
from datetime import datetime

LOG_FILENAME = datetime.now().strftime("%Y%m%d%H%M%S") + ".log"
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILENAME)
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILENAME)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="%(asctime)s -%(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
