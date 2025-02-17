# model_registry/model_tracker.py
from mlflow.tracking import MlflowClient
from mlflow.entities import ViewType
from typing import Dict, List
import pandas as pd

class ModelTracker:
    def __init__(self):
        self.client = MlflowClient()
    
    def get_model_versions(self, model_name: str) -> List[Dict]:
        """
        Get all versions of a model with their details
        """
        versions = self.client.search_model_versions(f"name='{model_name}'")
        return [
            {
                'version': version.version,
                'stage': version.current_stage,
                'creation_timestamp': version.creation_timestamp,
                'last_updated_timestamp': version.last_updated_timestamp,
                'metrics': self._get_version_metrics(version.run_id)
            }
            for version in versions
        ]
    
    def _get_version_metrics(self, run_id: str) -> Dict:
        """
        Get metrics for a specific model version
        """
        run = self.client.get_run(run_id)
        return run.data.metrics