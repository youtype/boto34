"""
Wrapper for aiobotocore ElasticLoadBalancingv2 service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_elbv2/)

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
    # Returns type annotated aiobotocore ElasticLoadBalancingv2 client
    async with session.elbv2.create_client() as elbv2_client:
        elbv2_client: types_aiobotocore_elbv2.client.ElasticLoadBalancingv2Client
    ```
"""

from __future__ import annotations

from types_aiobotocore_elbv2.client import ElasticLoadBalancingv2Client

from boto34.aiobotocore.service_factory import ServiceFactory


class ElasticLoadBalancingv2Service(ServiceFactory[ElasticLoadBalancingv2Client]):
    SERVICE_NAME = "elbv2"
    _SERVICE_PROP = "elbv2"
