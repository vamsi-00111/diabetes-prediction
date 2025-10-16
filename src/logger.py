import logging
import os
import sys
import datetime


logfile_name=os.path.join(f'{datetime.datetime.now().strftime("%y_%m_%d-%H_%M_%S")}.log')
logfile_path=os.path.join(os.getcwd(),"logs")
os.makedirs(logfile_path,exist_ok=True)

logfile=os.path.join(logfile_path,logfile_name)


logging.basicConfig(filename=logfile,
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                    level=logging.INFO,
                    )

    
    
    
