"""
Wrapper for aiobotocore CostOptimizationHub service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cost_optimization_hub/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore CostOptimizationHub client
    async with session.cost_optimization_hub.create_client() as cost_optimization_hub_client:
        cost_optimization_hub_client: (
            types_aiobotocore_cost_optimization_hub.client.CostOptimizationHubClient
        )
    ```
"""

from __future__ import annotations

from types_aiobotocore_cost_optimization_hub.client import CostOptimizationHubClient

from boto34.aiobotocore.service_factory import ServiceFactory


class CostOptimizationHubService(ServiceFactory[CostOptimizationHubClient]):
    SERVICE_NAME = "cost-optimization-hub"
    _SERVICE_PROP = "cost_optimization_hub"
