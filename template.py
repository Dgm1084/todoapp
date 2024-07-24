import os
from pathlib import Path
import logging
logging.basicConfig(level = logging.INFO, format = '[%(asctime)s]: %(message)s:')

project_name = "to_do_list_app"

# Define the directory to be created
filedir = 'C:\Users\e059955\projects\todoapp'

list_of_files = [
     f"{project_name}/user_service",
     f"{project_name}/user_service/app.py",
     f"{project_name}/user_service/requirements.txt",
     f"{project_name}/user_service/Dockerfile",
     f"{project_name}/task_service",
     f"{project_name}/task_service/app.py",
     f"{project_name}/task_service/requirements.txt",
     f"{project_name}/task_service/Dockerfile",
     f"{project_name}/docker-compose.yml"
]


for filepath in list_of_files:
    filepath = Path(filepath)

    filedir, filename = os.path.split(filepath)

    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")


    if(not os.path.exists(filename)) or (os.path.getsize(filename) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filename}")

    else:
        logging.info(f"{filename} is already created")

    
 
