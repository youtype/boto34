"""
Wrapper for aiobotocore QConnect service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/)

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
    # Returns type annotated aiobotocore QConnect client
    async with session.qconnect.create_client() as qconnect_client:
        qconnect_client: types_aiobotocore_qconnect.client.QConnectClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_qconnect.client import QConnectClient

from boto34.aiobotocore.service_factory import ServiceFactory


class QConnectService(ServiceFactory[QConnectClient]):
    SERVICE_NAME = "qconnect"
    _SERVICE_PROP = "qconnect"
