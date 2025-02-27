"""
Wrapper for aiobotocore EndUserMessagingSocial service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_socialmessaging/)

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
    # Returns type annotated aiobotocore EndUserMessagingSocial client
    async with session.socialmessaging.create_client() as socialmessaging_client:
        socialmessaging_client: types_aiobotocore_socialmessaging.client.EndUserMessagingSocialClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_socialmessaging.client import EndUserMessagingSocialClient

from boto34.aiobotocore.service_factory import ServiceFactory


class EndUserMessagingSocialService(ServiceFactory[EndUserMessagingSocialClient]):
    SERVICE_NAME = "socialmessaging"
    _SERVICE_PROP = "socialmessaging"
