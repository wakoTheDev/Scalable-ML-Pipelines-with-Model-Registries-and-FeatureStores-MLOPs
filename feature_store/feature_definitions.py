from datetime import timedelta
from feast import Entity, Feature, FeatureView, FileSource, Field
from feast.types import Float32, Int64

# Define your entity
customer = Entity(
    name="customer_id",
    join_keys=["customer_id"],
    description="customer identifier",
)

# Define your feature source
customer_stats_source = FileSource(
    path="data/customer_stats.parquet",
    timestamp_field="event_timestamp",
)

# Define your feature view with schema
customer_stats_view = FeatureView(
    name="customer_statistics",
    entities=[customer],
    ttl=timedelta(days=1),
    schema=[
        Field(name="total_purchases", dtype=Float32),
        Field(name="average_order_value", dtype=Float32),
        Field(name="days_since_last_purchase", dtype=Int64),
    ],
    source=customer_stats_source,
    online=True,
)