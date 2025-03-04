import logging
import os
from datetime import datetime

LOG_file = f"{datetime.now().strftime('%Y-%m-%d')}.log"
LOG_path = os.path.join(os.getcwd(), 'logs', LOG_file)  
os.makedirs(LOG_path, exist_ok=True)

LOG_file_path = os.path.join(LOG_path, LOG_file)
logging.basicConfig(
    filename=LOG_file_path,
    level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
level = {
    'info': logging.info,
    'debug': logging.debug,
    'warning': logging.warning,
    'error': logging.error,
    'critical': logging.critical
}

# if __name__ == '__main__':
#     level['info']('This is info message')
#     level['debug']('This is debug message')
#     level['warning']('This is warning message')
#     level['error']('This is error message')
#     level['critical']('This is critical message')
#     logging.info("Logging has started")
#     logging.debug("Logging has started")
#     logging.warning("Logging has started")
#     logging.error("Logging has started")