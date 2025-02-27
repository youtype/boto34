"""
Wrapper for aioboto3 IVS service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_ivs/)

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
    # Returns type annotated aioboto3 IVS client
    ivs_client = session.ivs.client()
    ivs_client: types_aiobotocore_ivs.client.IVSClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_ivs.client import IVSClient
except ImportError:
    IVSClient = object  # type: ignore[misc,assignment]


class IVSService(
    ServiceFactory[IVSClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "ivs"
    _SERVICE_PROP = "ivs"
