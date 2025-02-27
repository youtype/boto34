"""
Wrapper for aioboto3 Macie2 service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_macie2/)

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
    # Returns type annotated aioboto3 Macie2 client
    macie2_client = session.macie2.client()
    macie2_client: types_aiobotocore_macie2.client.Macie2Client
    ```
"""

from __future__ import annotations

from types_aiobotocore_macie2.client import Macie2Client

from boto34.aioboto3.service_factory import ServiceFactory


class Macie2Service(ServiceFactory[Macie2Client]):
    SERVICE_NAME = "macie2"
    _SERVICE_PROP = "macie2"
