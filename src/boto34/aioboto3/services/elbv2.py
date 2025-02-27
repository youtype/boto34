"""
Wrapper for aioboto3 ElasticLoadBalancingv2 service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_elbv2/)

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
    # Returns type annotated aioboto3 ElasticLoadBalancingv2 client
    elbv2_client = session.elbv2.client()
    elbv2_client: types_aiobotocore_elbv2.client.ElasticLoadBalancingv2Client
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_elbv2.client import ElasticLoadBalancingv2Client
except ImportError:
    ElasticLoadBalancingv2Client = object  # type: ignore[misc,assignment]


class ElasticLoadBalancingv2Service(
    ServiceFactory[ElasticLoadBalancingv2Client]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "elbv2"
    _SERVICE_PROP = "elbv2"
