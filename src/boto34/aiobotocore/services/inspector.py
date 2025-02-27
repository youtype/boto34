"""
Wrapper for aiobotocore Inspector service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector/)

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
    # Returns type annotated aiobotocore Inspector client
    async with session.inspector.create_client() as inspector_client:
        inspector_client: types_aiobotocore_inspector.client.InspectorClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_inspector.client import InspectorClient
except ImportError:
    InspectorClient = object  # type: ignore[misc,assignment]


class InspectorService(
    ServiceFactory[InspectorClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "inspector"
    _SERVICE_PROP = "inspector"
