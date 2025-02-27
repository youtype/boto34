"""
Wrapper for aioboto3 CostOptimizationHub service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_cost_optimization_hub/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aioboto3 import Session

    # Wrapper for aioboto3.Session constructor
    # Returns boto34.Session inherited from aioboto3.Session
    session = Session()
    session: boto34.aioboto3.session.Session

    # Type annotated aioboto3.Client
    # Uses the same arguments as aioboto3.client method
    # Returns type annotated aioboto3 CostOptimizationHub client
    cost_optimization_hub_client = session.cost_optimization_hub.client()
    cost_optimization_hub_client: (
        types_aiobotocore_cost_optimization_hub.client.CostOptimizationHubClient
    )
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_cost_optimization_hub.client import CostOptimizationHubClient
except ImportError:
    CostOptimizationHubClient = object  # type: ignore[misc,assignment]


class CostOptimizationHubService(
    ServiceFactory[CostOptimizationHubClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "cost-optimization-hub"
    _SERVICE_PROP = "cost_optimization_hub"
