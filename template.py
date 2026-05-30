# import os
# from pathlib import Path
# import logging

# logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# list_of_files = [
#     "src/__init__.py",
#     "src/helper.py",
#     "src/prompt.py",
#     ".env",
#     "requirements.txt",
#     "setup.py",
#     "research/trials.ipynb" ,
#     "app.py"
    
# ]
# for filepath in list_of_files:
#     filepath= Path(filepath)
#     filedir,filename = os.path.split(filepath)

# if filepath !="":
#     os.makedirs(filedir,exist_ok=True)
#     logging.info(f"create directory; {filedir} for the file: {filename}")
    
# if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
#     with open(filepath, "w") as f:
#         pass
#         logging.info(f"creating empty file:{filepath}")
    
# else:
#     logging.info(f"{filename} is already exists")
    
    
#  best way for creating multiple file 
    
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "app.py"
]

for file in files:
    path = Path(file)

    path.parent.mkdir(parents=True, exist_ok=True)

    if not path.exists():
        path.touch()
        logging.info(f"Created: {path}")