"""
Wrapper for aiobotocore CloudWatchRUM service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rum/)

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
    # Returns type annotated aiobotocore CloudWatchRUM client
    async with session.rum.create_client() as rum_client:
        rum_client: types_aiobotocore_rum.client.CloudWatchRUMClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_rum.client import CloudWatchRUMClient

from boto34.aiobotocore.service_factory import ServiceFactory


class CloudWatchRUMService(ServiceFactory[CloudWatchRUMClient]):
    SERVICE_NAME = "rum"
    _SERVICE_PROP = "rum"
