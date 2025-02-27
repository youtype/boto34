"""
Wrapper for aiobotocore Lightsail service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lightsail/)

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
    # Returns type annotated aiobotocore Lightsail client
    async with session.lightsail.create_client() as lightsail_client:
        lightsail_client: types_aiobotocore_lightsail.client.LightsailClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_lightsail.client import LightsailClient

from boto34.aiobotocore.service_factory import ServiceFactory


class LightsailService(ServiceFactory[LightsailClient]):
    SERVICE_NAME = "lightsail"
    _SERVICE_PROP = "lightsail"
