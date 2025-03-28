import logging
import os
from datetime import datetime


#.log is an extenssion
#A file path with log extention
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"   

#getcwd = get current working directory
#logs is a folder name that will create in current working directory folder (root folder)
log_path=os.path.join(os.getcwd(),"logs")     

#create logs folder according to previous path
os.makedirs(log_path,exist_ok=True)


#the path of of log_file (.log file) inside the logs folder 
LOG_FILEPATH=os.path.join(log_path,LOG_FILE)

#create the LOG_FILE (.log file) inside the logs folder
logging.basicConfig(level=logging.INFO, 
        filename=LOG_FILEPATH,
        format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)