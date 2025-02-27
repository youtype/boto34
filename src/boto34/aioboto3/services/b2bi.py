"""
Wrapper for aioboto3 B2BI service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_b2bi/)

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
    # Returns type annotated aioboto3 B2BI client
    b2bi_client = session.b2bi.client()
    b2bi_client: types_aiobotocore_b2bi.client.B2BIClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_b2bi.client import B2BIClient
except ImportError:
    B2BIClient = object  # type: ignore[misc,assignment]


class B2BIService(
    ServiceFactory[B2BIClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "b2bi"
    _SERVICE_PROP = "b2bi"
