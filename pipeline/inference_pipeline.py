from feast import FeatureStore
from model_registry.model_manager import ModelManager

class InferencePipeline:
    def __init__(self):
        self.feature_store = FeatureStore("")
        self.model_manager = ModelManager()
        self.model = self.model_manager.get_production_model("customer_prediction_model")
    
    def get_online_features(self, customer_ids):
        """Get online features from feature store"""
        features = self.feature_store.get_online_features(
            entity_rows=[{"customer_id": id} for id in customer_ids],
            features=[
                "customer_statistics:total_purchases",
                "customer_statistics:average_order_value",
                "customer_statistics:days_since_last_purchase",
            ],
        ).to_dict()
        return features
    
    def predict(self, customer_ids):
        """Make predictions using production model"""
        features = self.get_online_features(customer_ids)
        predictions = self.model.predict(features)
        return predictions