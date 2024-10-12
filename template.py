import os 
from pathlib import Path 



package_name = "mongodb_connect"


list_of_files = [

    '.github/workflows/ci.yaml',
    'src/__init__.py',  
    f'src/{package_name}/__init__.py' ,
    f'src/{package_name}/mongo_crub.py' , 
    'src/components/data_ingestion.py' , 
    'src/components/data_transformation.py' , 
    'src/components/model_trainer.py' ,  
    'src/components/model_monitering.py' , 
    'src/components/model_evaluation.py' ,  
    'src/pipeline/__init__.py' ,  
    'src/pipeline/training_pipeline.py' ,
    'src/pipeline/prediction_pipeline.py' ,  
    'src/utils/utils.py' , 
    'tests/unit/unit.py' , 
    'tests/integration/__init__.py' ,
    'init_setup.sh' , 
    'requirements.txt' ,  
    'experiment/experiments.ipynb' , 
    'setup.py' , 
    'setup.cfg' , 
    'pyproject.toml' ,
    'tox.ini' , 
    

]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath) 
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            
