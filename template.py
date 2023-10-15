import os
from pathlib import Path
import logging

logging.basicConfig(
    level= logging.INFO,
    filename="template_structure.log",
    filemode='w',
    format= '%(asctime)s - %(message)s',
    datefmt='%d-%b-%y %H:%M:%S'
)

while True:
    Project_name = input("Enter your project name: ")
    if Project_name !='':
        break

logging.info(f"Creating project by name: {Project_name}")

list_of_files = [
    f"src/{Project_name}/__init__.py",
    f"src/{Project_name}/utils/__init__.py",
    f"src/{Project_name}/config/__init__.py",
    f"src/{Project_name}/components/__init__.py",
    f"src/{Project_name}/config/configuration.py",
    f"src/{Project_name}/pipeline/__init__.py",
    f"src/{Project_name}/entity/__init__.py",
    f"src/{Project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "templates/index.html"
]

for filepath in list_of_files:
    filepath = Path(filepath) 
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")

    if (not os.path.exists(filepath) or (os.path.getsize(filepath) == 0)):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")

logging.info("Project Structure is completed") 