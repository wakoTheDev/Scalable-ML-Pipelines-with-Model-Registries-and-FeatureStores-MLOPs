import mlflow
from datetime import datetime

class MetricsTracker:
    def __init__(self):
        self.client = mlflow.tracking.MlflowClient()
    
    def log_prediction_metrics(self, model_name, metrics):
        """Log prediction metrics to MLflow"""
        run = mlflow.start_run()
        
        # Log metrics with timestamp
        for metric_name, metric_value in metrics.items():
            mlflow.log_metric(
                metric_name,
                metric_value,
                step=int(datetime.now().timestamp())
            )
        
        mlflow.end_run()
    
    def get_metric_history(self, model_name, metric_name):
        """Get historical metrics for a model"""
        runs = self.client.search_runs(
            experiment_ids=[mlflow.get_experiment_by_name(model_name).experiment_id]
        )
        
        metric_history = []
        for run in runs:
            if metric_name in run.data.metrics:
                metric_history.append({
                    'timestamp': run.info.start_time,
                    'value': run.data.metrics[metric_name]
                })
        
        return metric_history