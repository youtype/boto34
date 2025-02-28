"""
Wrapper for aioboto3 ElasticLoadBalancingv2 service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_elbv2/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_elbv2.client import ElasticLoadBalancingv2Client

from boto34.aioboto3.service_factory import ServiceFactory


class ElasticLoadBalancingv2Service(ServiceFactory[ElasticLoadBalancingv2Client]):
    """
    ElasticLoadBalancingv2 service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_elbv2/)
    """
