"""
Wrapper for aiobotocore QBusiness service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/)

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
    # Returns type annotated aiobotocore QBusiness client
    async with session.qbusiness.create_client() as qbusiness_client:
        qbusiness_client: types_aiobotocore_qbusiness.client.QBusinessClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_qbusiness.client import QBusinessClient

from boto34.aiobotocore.service_factory import ServiceFactory


class QBusinessService(ServiceFactory[QBusinessClient]):
    SERVICE_NAME = "qbusiness"
    _SERVICE_PROP = "qbusiness"
