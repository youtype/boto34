"""
Wrapper for aioboto3 Cloud9 service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_cloud9/)

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
    # Returns type annotated aioboto3 Cloud9 client
    cloud9_client = session.cloud9.client()
    cloud9_client: types_aiobotocore_cloud9.client.Cloud9Client
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_cloud9.client import Cloud9Client
except ImportError:
    Cloud9Client = object  # type: ignore[misc,assignment]


class Cloud9Service(
    ServiceFactory[Cloud9Client]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "cloud9"
    _SERVICE_PROP = "cloud9"
