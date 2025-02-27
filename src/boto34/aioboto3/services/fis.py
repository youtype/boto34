"""
Wrapper for aioboto3 FIS service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_fis/)

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
    # Returns type annotated aioboto3 FIS client
    fis_client = session.fis.client()
    fis_client: types_aiobotocore_fis.client.FISClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_fis.client import FISClient

from boto34.aioboto3.service_factory import ServiceFactory


class FISService(ServiceFactory[FISClient]):
    SERVICE_NAME = "fis"
    _SERVICE_PROP = "fis"
