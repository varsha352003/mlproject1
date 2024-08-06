import logging
import os
from datetime import datetime
# Define log file name with a timestamp
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define log file path
log_path=os.path.join(os.getcwd(),"logs",LOG_FILE)

# Create the logs directory if it does not exist
os.makedirs(log_path,exist_ok=True)

# Define the complete path for the log file
LOG_FILE_PATH=os.path.join(log_path,LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
