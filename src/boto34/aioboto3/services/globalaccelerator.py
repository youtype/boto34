"""
Wrapper for aioboto3 GlobalAccelerator service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_globalaccelerator/)

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
    # Returns type annotated aioboto3 GlobalAccelerator client
    globalaccelerator_client = session.globalaccelerator.client()
    globalaccelerator_client: types_aiobotocore_globalaccelerator.client.GlobalAcceleratorClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_globalaccelerator.client import GlobalAcceleratorClient
except ImportError:
    GlobalAcceleratorClient = object  # type: ignore[misc,assignment]


class GlobalAcceleratorService(
    ServiceFactory[GlobalAcceleratorClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "globalaccelerator"
    _SERVICE_PROP = "globalaccelerator"
