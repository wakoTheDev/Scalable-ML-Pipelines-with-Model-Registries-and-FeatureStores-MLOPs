from datetime import datetime, timedelta

class FeastConfig:
    ONLINE_STORE = {
        "type": "redis",
        "connection_string":"localhost:6379",
    }
    
    OFFLINE_STORE = {
        "type":"file",
        "path": "data/offline_store",
    }
    
    FEATURE_TTL = timedelta(days=1)
    PROJECT_NAME = "production_features"