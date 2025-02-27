"""
Wrapper for aiobotocore DirectConnect service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_directconnect/)

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
    # Returns type annotated aiobotocore DirectConnect client
    async with session.directconnect.create_client() as directconnect_client:
        directconnect_client: types_aiobotocore_directconnect.client.DirectConnectClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_directconnect.client import DirectConnectClient

from boto34.aiobotocore.service_factory import ServiceFactory


class DirectConnectService(ServiceFactory[DirectConnectClient]):
    SERVICE_NAME = "directconnect"
    _SERVICE_PROP = "directconnect"
