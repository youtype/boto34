"""
Wrapper for aioboto3 Detective service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_detective/)

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
    # Returns type annotated aioboto3 Detective client
    detective_client = session.detective.client()
    detective_client: types_aiobotocore_detective.client.DetectiveClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_detective.client import DetectiveClient
except ImportError:
    DetectiveClient = object  # type: ignore[misc,assignment]


class DetectiveService(
    ServiceFactory[DetectiveClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "detective"
    _SERVICE_PROP = "detective"
