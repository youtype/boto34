"""
Wrapper for aioboto3 CostOptimizationHub service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_cost_optimization_hub/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_cost_optimization_hub.client import CostOptimizationHubClient

from boto34.aioboto3.service_factory import ServiceFactory


class CostOptimizationHubService(ServiceFactory[CostOptimizationHubClient]):
    """
    CostOptimizationHub service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_cost_optimization_hub/)
    """
