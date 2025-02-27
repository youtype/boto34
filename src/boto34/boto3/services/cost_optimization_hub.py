"""
Wrapper for boto3 CostOptimizationHub service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cost_optimization_hub/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.boto3 import Session

    # Wrapper for boto3.Session constructor
    # Returns boto34.Session inherited from boto3.Session
    session = Session()
    session: boto34.boto3.session.Session

    # Type annotated boto3.Client
    # Uses the same arguments as boto3.client method
    # Returns type annotated boto3 CostOptimizationHub client
    cost_optimization_hub_client = session.cost_optimization_hub.client()
    cost_optimization_hub_client: types_boto3_cost_optimization_hub.client.CostOptimizationHubClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_cost_optimization_hub.client import CostOptimizationHubClient
except ImportError:
    CostOptimizationHubClient = object  # type: ignore[misc,assignment]


class CostOptimizationHubService(
    ServiceFactory[CostOptimizationHubClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "cost-optimization-hub"
    _SERVICE_PROP = "cost_optimization_hub"
