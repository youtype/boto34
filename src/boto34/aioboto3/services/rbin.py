"""
Wrapper for aioboto3 RecycleBin service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_rbin/)

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
    # Returns type annotated aioboto3 RecycleBin client
    rbin_client = session.rbin.client()
    rbin_client: types_aiobotocore_rbin.client.RecycleBinClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_rbin.client import RecycleBinClient

from boto34.aioboto3.service_factory import ServiceFactory


class RecycleBinService(ServiceFactory[RecycleBinClient]):
    SERVICE_NAME = "rbin"
    _SERVICE_PROP = "rbin"
