"""
Wrapper for aioboto3 SESV2 service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_sesv2/)

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
    # Returns type annotated aioboto3 SESV2 client
    sesv2_client = session.sesv2.client()
    sesv2_client: types_aiobotocore_sesv2.client.SESV2Client
    ```
"""

from __future__ import annotations

from types_aiobotocore_sesv2.client import SESV2Client

from boto34.aioboto3.service_factory import ServiceFactory


class SESV2Service(ServiceFactory[SESV2Client]):
    SERVICE_NAME = "sesv2"
    _SERVICE_PROP = "sesv2"
