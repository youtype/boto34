"""
Wrapper for aioboto3 XRay service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_xray/)

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
    # Returns type annotated aioboto3 XRay client
    xray_client = session.xray.client()
    xray_client: types_aiobotocore_xray.client.XRayClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_xray.client import XRayClient

from boto34.aioboto3.service_factory import ServiceFactory


class XRayService(ServiceFactory[XRayClient]):
    SERVICE_NAME = "xray"
    _SERVICE_PROP = "xray"
