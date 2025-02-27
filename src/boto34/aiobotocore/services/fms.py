"""
Wrapper for aiobotocore FMS service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_fms/)

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
    # Returns type annotated aiobotocore FMS client
    async with session.fms.create_client() as fms_client:
        fms_client: types_aiobotocore_fms.client.FMSClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_fms.client import FMSClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_fms.client import FMSClient
except ImportError:
    FMSClient = object  # type: ignore[misc,assignment]


class FMSService(
    ServiceFactory[FMSClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "fms"
    _SERVICE_PROP = "fms"
