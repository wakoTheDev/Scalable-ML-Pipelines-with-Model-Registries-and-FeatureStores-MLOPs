import os
from dotenv import load_dotenv
import mlflow
from config import MLflowConfig, FeastConfig
from feature_store import FeatureService
from model_registry import ModelManager, ModelTracker
from pipeline import TrainingPipeline, InferencePipeline
from monitoring import MetricsTracker

def initialize_mlops_environment():
    """
    Initialize the MLOps environment with all necessary components
    """
    # Load environment variables
    load_dotenv()
    
    print(MLflowConfig.MLFLOW_TRACKING_URI)
    
    # Set up MLflow
    mlflow.set_tracking_uri(MLflowConfig.MLFLOW_TRACKING_URI)
    
    # Initialize components
    feature_service = FeatureService()
    model_manager = ModelManager()
    model_tracker = ModelTracker()
    metrics_tracker = MetricsTracker()
    
    return {
        'feature_service': feature_service,
        'model_manager': model_manager,
        'model_tracker': model_tracker,
        'metrics_tracker': metrics_tracker
    }

if __name__ == "__main__":
    # Initialize environment
    components = initialize_mlops_environment()
    
    # Create training and inference pipelines
    training_pipeline = TrainingPipeline()
    inference_pipeline = InferencePipeline()