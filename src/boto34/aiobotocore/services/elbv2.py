"""
Wrapper for aiobotocore ElasticLoadBalancingv2 service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_elbv2/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_elbv2.client import ElasticLoadBalancingv2Client

from boto34.aiobotocore.service_factory import ServiceFactory


class ElasticLoadBalancingv2Service(ServiceFactory[ElasticLoadBalancingv2Client]):
    """
    ElasticLoadBalancingv2 service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_elbv2/)
    """
