from feast import FeatureStore
from model_registry.model_manager import ModelManager
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import os


class TrainingPipeline:
    def __init__(self):
        
        self.feature_store = FeatureStore("")
        self.model_manager = ModelManager()
    
    def get_training_data(self, entity_df):
        """Get training data from feature store"""
        training_data = self.feature_store.get_historical_features(
            entity_df=entity_df,
            features=[
                "customer_statistics:total_purchases",
                "customer_statistics:average_order_value",
                "customer_statistics:days_since_last_purchase",
            ],
        ).to_df()
        return training_data
    
    def train_model(self, model, training_data, target_column):
        """Train and register model"""
        X = training_data.drop(columns=[target_column])
        y = training_data[target_column]
        
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        model.fit(X_train, y_train)
        print("model trained ...")
        
        # Calculate metrics
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        
        # Register model
        self.model_manager.register_model(
            model=model,
            model_name="customer_prediction_model",
            metrics={"accuracy": accuracy}
        )
        print("model saved ...")
        return model, accuracy