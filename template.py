import os
from pathlib import Path # import path class from the pathlib module

list_of_files = [
    ".github/workflows/.gitkeep",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction__pipeline.py",
    "src/utils/__init.py",
    "src/utils/utils.py",
    "src/logger/logging.py",
    "src/exception/exception.py",
    "tests/unit/__init.py",
    "tests/integration/__init.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiment/experiments.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)  #convert file path string to Path object for easier manipulation
    filedir, filename = os.path.split(filepath) # spilit the filepath into the directory part(filedir) and file name part(Filename)
    if filedir != "": # checks if the filedir is not empty string
        os.makedirs(filedir, exist_ok=True)
    if (not os.path.exists(filepath) or os.path.getsize(filepath) == 0):
       with open(filepath, "w") as f:
           pass #create an empty file