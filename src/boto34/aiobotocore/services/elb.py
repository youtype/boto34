"""
Wrapper for aiobotocore ElasticLoadBalancing service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_elb/)

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
    # Returns type annotated aiobotocore ElasticLoadBalancing client
    async with session.elb.create_client() as elb_client:
        elb_client: types_aiobotocore_elb.client.ElasticLoadBalancingClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_elb.client import ElasticLoadBalancingClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_elb.client import ElasticLoadBalancingClient
except ImportError:
    ElasticLoadBalancingClient = object  # type: ignore[misc,assignment]


class ElasticLoadBalancingService(
    ServiceFactory[ElasticLoadBalancingClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "elb"
    _SERVICE_PROP = "elb"
