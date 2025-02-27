"""
Wrapper for aiobotocore ServiceDiscovery service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_servicediscovery/)

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
    # Returns type annotated aiobotocore ServiceDiscovery client
    async with session.servicediscovery.create_client() as servicediscovery_client:
        servicediscovery_client: types_aiobotocore_servicediscovery.client.ServiceDiscoveryClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_servicediscovery.client import ServiceDiscoveryClient

from boto34.aiobotocore.service_factory import ServiceFactory


class ServiceDiscoveryService(ServiceFactory[ServiceDiscoveryClient]):
    SERVICE_NAME = "servicediscovery"
    _SERVICE_PROP = "servicediscovery"
