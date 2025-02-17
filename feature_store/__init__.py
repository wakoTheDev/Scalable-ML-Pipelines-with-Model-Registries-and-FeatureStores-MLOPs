# feature_store/__init__.py
from .feature_service import (
    FeatureService,
    customer,
    customer_stats_view,
    initialize_feature_store
)

__all__ = [
    'FeatureService',
    'customer',
    'customer_stats_view',
    'initialize_feature_store'
]