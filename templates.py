import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:') #to check logs

projectname= "text_classifier"

list_folders= [
    ".github/workflows/.gitkeep",
    f"src/{projectname}/__init__.py",  #for local package constructor package
    f"src/{projectname}/components/__init__.py",  
    f"src/{projectname}/utils/__init__.py",
    f"src/{projectname}/utils/common.py",
    f"src/{projectname}/logging/__init__.py",
    f"src/{projectname}/config/__init__.py",
    f"src/{projectname}/config/configuration.py",
    f"src/{projectname}/pipeline/__init__.py",
    f"src/{projectname}/pipeline/configuration.py",
    f"src/{projectname}/entity/__init__.py",
    f"src/{projectname}/constants/__init__.py",
    "config/config.yaml",
    "app.py",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "main.py",
    "Dockerfile",
    "reasearch/trials.ipynb",
    "templates/index.html"

]

# creating files and folder
for filepath in list_folders:
    filepath = Path(filepath)  # showing the window path
    filedir,filename=os.path.split(filepath) # shole folder and filename

    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating dir:{filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file : {filepath}")
    else:
        logging.info(f"{filename} already exist")