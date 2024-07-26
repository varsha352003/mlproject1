import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"  ##month days year hr min sec, .log is extension of this file
log_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
##getcwd= get current working directory, folder name log in which our logs_file will be made

os.makedirs(log_path,exist_ok=True)
##if folder is already avl then skip
LOG_FILE_PATH=os.path.join(log_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

##format is how the log msg will show
##the msg for eg. file has been created will be shown in message
##lineno is in which line it's executing
##level is loggging.info but we can set .error or .warning
