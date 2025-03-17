

from prometheus_client import Summary
from models.definition import Definition

def transform_to_prometheus_metrics(metric_name: str, metric: dict[str, list[str, any]], metric_doc: str = ""):
    s = Summary(metric_name, metric_doc, ['name', 'description', 'type', 'required'])
    print(s)
    return False