"""
Wrapper for aiobotocore ElasticLoadBalancing service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_elb/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_elb.client import ElasticLoadBalancingClient

from boto34.aiobotocore.service_factory import ServiceFactory


class ElasticLoadBalancingService(ServiceFactory[ElasticLoadBalancingClient]):
    """
    ElasticLoadBalancing service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_elb/)
    """
