"""
Wrapper for aioboto3 Kendra service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_kendra/)

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
    # Returns type annotated aioboto3 Kendra client
    kendra_client = session.kendra.client()
    kendra_client: types_aiobotocore_kendra.client.KendraClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_kendra.client import KendraClient
except ImportError:
    KendraClient = object  # type: ignore[misc,assignment]


class KendraService(
    ServiceFactory[KendraClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "kendra"
    _SERVICE_PROP = "kendra"
