"""
Wrapper for aiobotocore XRay service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_xray/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore XRay client
    async with session.xray.create_client() as xray_client:
        xray_client: types_aiobotocore_xray.client.XRayClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_xray.client import XRayClient

from boto34.aiobotocore.service_factory import ServiceFactory


class XRayService(ServiceFactory[XRayClient]):
    SERVICE_NAME = "xray"
    _SERVICE_PROP = "xray"
