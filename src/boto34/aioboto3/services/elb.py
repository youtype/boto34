"""
Wrapper for aioboto3 ElasticLoadBalancing service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_elb/)

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
    # Returns type annotated aioboto3 ElasticLoadBalancing client
    elb_client = session.elb.client()
    elb_client: types_aiobotocore_elb.client.ElasticLoadBalancingClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_elb.client import ElasticLoadBalancingClient
except ImportError:
    ElasticLoadBalancingClient = object  # type: ignore[misc,assignment]


class ElasticLoadBalancingService(
    ServiceFactory[ElasticLoadBalancingClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "elb"
    _SERVICE_PROP = "elb"
