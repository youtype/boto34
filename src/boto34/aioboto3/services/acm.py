"""
Wrapper for aioboto3 ACM 14.0.0 service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_acm/)

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
    # Returns type annotated aioboto3 ACM client
    acm_client = session.acm.client()
    acm_client: types_aiobotocore_acm.client.ACMClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_acm.client import ACMClient
except ImportError:
    ACMClient = object  # type: ignore[misc,assignment]


class ACMService(
    ServiceFactory[ACMClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "acm"
    _SERVICE_PROP = "acm"
