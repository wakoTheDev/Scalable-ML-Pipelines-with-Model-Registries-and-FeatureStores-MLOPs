import os
from dotenv import load_dotenv

load_dotenv()

class MLflowConfig:
    MLFLOW_TRACKING_URI =  os.getenv("MLFLOW_TRACKING_URI","http://localhost:5000")
    MLFLOW_EXPERIMENT_NAME =  os.getenv("MLFLOW_EXPERIMENT_NAME","production_model")
    MLFLOW_REGISTRY_URI=  os.getenv("MLFLOW_REGISTRY_URI","sqlite:///mlflow.db")