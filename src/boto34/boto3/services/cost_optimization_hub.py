"""
Wrapper for boto3 CostOptimizationHub service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cost_optimization_hub/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_cost_optimization_hub.client import CostOptimizationHubClient

from boto34.boto3.service_factory import ServiceFactory


class CostOptimizationHubService(ServiceFactory[CostOptimizationHubClient]):
    """
    CostOptimizationHub service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cost_optimization_hub/)
    """
