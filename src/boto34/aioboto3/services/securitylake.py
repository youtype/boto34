"""
Wrapper for aioboto3 SecurityLake service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_securitylake/)

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
    # Returns type annotated aioboto3 SecurityLake client
    securitylake_client = session.securitylake.client()
    securitylake_client: types_aiobotocore_securitylake.client.SecurityLakeClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_securitylake.client import SecurityLakeClient
except ImportError:
    SecurityLakeClient = object  # type: ignore[misc,assignment]


class SecurityLakeService(
    ServiceFactory[SecurityLakeClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "securitylake"
    _SERVICE_PROP = "securitylake"
