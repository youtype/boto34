"""
Wrapper for aioboto3 FSx service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_fsx/)

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
    # Returns type annotated aioboto3 FSx client
    fsx_client = session.fsx.client()
    fsx_client: types_aiobotocore_fsx.client.FSxClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_fsx.client import FSxClient
except ImportError:
    FSxClient = object  # type: ignore[misc,assignment]


class FSxService(
    ServiceFactory[FSxClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "fsx"
    _SERVICE_PROP = "fsx"
