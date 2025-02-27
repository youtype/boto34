"""
Wrapper for aiobotocore SESV2 service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sesv2/)

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
    # Returns type annotated aiobotocore SESV2 client
    async with session.sesv2.create_client() as sesv2_client:
        sesv2_client: types_aiobotocore_sesv2.client.SESV2Client
    ```
"""

from __future__ import annotations

from types_aiobotocore_sesv2.client import SESV2Client

from boto34.aiobotocore.service_factory import ServiceFactory


class SESV2Service(ServiceFactory[SESV2Client]):
    SERVICE_NAME = "sesv2"
    _SERVICE_PROP = "sesv2"
