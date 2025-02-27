"""
Wrapper for aioboto3 Support service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_support/)

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
    # Returns type annotated aioboto3 Support client
    support_client = session.support.client()
    support_client: types_aiobotocore_support.client.SupportClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_support.client import SupportClient
except ImportError:
    SupportClient = object  # type: ignore[misc,assignment]


class SupportService(
    ServiceFactory[SupportClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "support"
    _SERVICE_PROP = "support"
