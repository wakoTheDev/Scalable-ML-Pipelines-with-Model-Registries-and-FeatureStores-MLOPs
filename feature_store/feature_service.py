# feature_store/feature_service.py
from datetime import timedelta
from feast import (
    Entity, 
    FeatureView, 
    FileSource, 
    Field, 
    ValueType,
    FeatureService
)
from feast.types import Float32, Int64
import os
import pandas as pd
import numpy as np
from datetime import datetime

# Define entity with explicit value type
customer = Entity(
    name="customer",
    value_type=ValueType.INT64,
    join_keys=["customer_id"],
    description="customer identifier"
)

# Define source
customer_source = FileSource(
    path="data/customer_stats.parquet",
    timestamp_field="event_timestamp",
)

# Define feature view with explicit entity object
customer_stats_view = FeatureView(
    name="customer_statistics",
    entities=[customer],
    ttl=timedelta(days=1),
    schema=[
        Field(name="total_purchases", dtype=Float32),
        Field(name="average_order_value", dtype=Float32),
        Field(name="days_since_last_purchase", dtype=Int64),
    ],
    source=customer_source,
    online=True
)

def create_feature_store_yaml():
    """Create feature_store.yaml with minimal required configuration"""
    yaml_content = """
project: customer_features
provider: local
registry: data/registry.db
online_store:
    type: sqlite
    path: data/online_store.db
entity_key_serialization_version: 2 
"""
    with open('feature_store.yaml', 'w') as f:
        f.write(yaml_content.strip())

def create_sample_data():
    """Create sample data"""
    os.makedirs("data", exist_ok=True)
    
    n_customers = 100
    current_time = datetime.now()
    
    data = pd.DataFrame({
        'customer_id': range(n_customers),
        'event_timestamp': [current_time - timedelta(days=x) for x in range(n_customers)],
        'total_purchases': np.random.uniform(1, 100, n_customers),
        'average_order_value': np.random.uniform(10, 1000, n_customers),
        'days_since_last_purchase': np.random.randint(1, 365, n_customers)
    })
    
    # Convert types
    data['customer_id'] = data['customer_id'].astype('int64')
    data['total_purchases'] = data['total_purchases'].astype('float32')
    data['average_order_value'] = data['average_order_value'].astype('float32')
    data['days_since_last_purchase'] = data['days_since_last_purchase'].astype('int64')
    
    # Create data directory if it doesn't exist
    os.makedirs('data', exist_ok=True)
    
    # Save as parquet
    output_path = 'data/customer_stats.parquet'
    data.to_parquet(output_path, index=False)
    print(f"Sample data created at {output_path}")
    print("\nFirst few rows:")
    print(data.head())
    return data

class FeatureService:
    def __init__(self):
        from feast import FeatureStore
        self.store = FeatureStore(repo_path=".")
        
    def get_online_features(self, customer_ids):
        """Get online features for specific customers"""
        entity_rows = [{"customer_id": customer_id} for customer_id in customer_ids]
        features = [
            "customer_statistics:total_purchases",
            "customer_statistics:average_order_value",
            "customer_statistics:days_since_last_purchase",
        ]
        return self.store.get_online_features(
            entity_rows=entity_rows,
            features=features
        ).to_dict()

def initialize_feature_store():
    """Initialize the feature store"""
    try:
        # Create feature store config
        create_feature_store_yaml()
        
        # Create sample data
        create_sample_data()
        
        # Initialize and apply feature definitions
        from feast import FeatureStore
        store = FeatureStore(repo_path=".")
        store.apply([customer, customer_stats_view])
        
        print("Feature store initialized successfully!")
        return store
    except Exception as e:
        print(f"Error initializing feature store: {str(e)}")
        raise

if __name__ == "__main__":
    # Import and check Feast version
    import feast
    print(f"Using Feast version: {feast.__version__}")
    
    try:
        store = initialize_feature_store()
        print("Feature definitions applied successfully!")
    except Exception as e:
        print(f"Failed to initialize feature store: {str(e)}")