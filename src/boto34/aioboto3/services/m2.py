"""
Wrapper for aioboto3 MainframeModernization service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_m2/)

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
    # Returns type annotated aioboto3 MainframeModernization client
    m2_client = session.m2.client()
    m2_client: types_aiobotocore_m2.client.MainframeModernizationClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_m2.client import MainframeModernizationClient
except ImportError:
    MainframeModernizationClient = object  # type: ignore[misc,assignment]


class MainframeModernizationService(
    ServiceFactory[MainframeModernizationClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "m2"
    _SERVICE_PROP = "m2"
