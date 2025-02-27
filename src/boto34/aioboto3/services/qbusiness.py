"""
Wrapper for aioboto3 QBusiness service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_qbusiness/)

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
    # Returns type annotated aioboto3 QBusiness client
    qbusiness_client = session.qbusiness.client()
    qbusiness_client: types_aiobotocore_qbusiness.client.QBusinessClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_qbusiness.client import QBusinessClient

from boto34.aioboto3.service_factory import ServiceFactory


class QBusinessService(ServiceFactory[QBusinessClient]):
    SERVICE_NAME = "qbusiness"
    _SERVICE_PROP = "qbusiness"
