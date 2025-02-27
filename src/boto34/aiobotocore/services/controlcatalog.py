"""
Wrapper for aiobotocore ControlCatalog service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_controlcatalog/)

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
    # Returns type annotated aiobotocore ControlCatalog client
    async with session.controlcatalog.create_client() as controlcatalog_client:
        controlcatalog_client: types_aiobotocore_controlcatalog.client.ControlCatalogClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_controlcatalog.client import ControlCatalogClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_controlcatalog.client import ControlCatalogClient
except ImportError:
    ControlCatalogClient = object  # type: ignore[misc,assignment]


class ControlCatalogService(
    ServiceFactory[ControlCatalogClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "controlcatalog"
    _SERVICE_PROP = "controlcatalog"
