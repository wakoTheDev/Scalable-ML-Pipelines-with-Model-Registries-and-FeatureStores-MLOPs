import mlflow
from mlflow.tracking import MlflowClient
from config.mlflow_config import MLflowConfig

class ModelManager:
    def __init__(self):
        mlflow.set_tracking_uri(MLflowConfig.MLFLOW_TRACKING_URI)
        self.client = MlflowClient()
        self.experiment_name = MLflowConfig.MLFLOW_EXPERIMENT_NAME
        
    def register_model(self, model, model_name, metrics):
        """Register a new model version with MLflow"""
        mlflow.set_experiment(self.experiment_name)
        
        with mlflow.start_run():
            # Log model metrics
            for metric_name, metric_value in metrics.items():
                mlflow.log_metric(metric_name, metric_value)
            
            # Log model
            mlflow.sklearn.log_model(
                model,
                "model",
                registered_model_name=model_name
            )
    
    def transition_model_stage(self, model_name, version, stage):
        """Transition a model version to a new stage"""
        self.client.transition_model_version_stage(
            name=model_name,
            version=version,
            stage=stage
        )
    
    def get_production_model(self, model_name):
        """Get the current production model"""
        model_version = self.client.get_latest_versions(
            model_name, 
            stages=["Production"]
        )[0]
        return mlflow.pyfunc.load_model(model_version.source)
