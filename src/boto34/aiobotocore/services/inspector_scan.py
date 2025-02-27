"""
Wrapper for aiobotocore Inspectorscan service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector_scan/)

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
    # Returns type annotated aiobotocore Inspectorscan client
    async with session.inspector_scan.create_client() as inspector_scan_client:
        inspector_scan_client: types_aiobotocore_inspector_scan.client.InspectorscanClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_inspector_scan.client import InspectorscanClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_inspector_scan.client import InspectorscanClient
except ImportError:
    InspectorscanClient = object  # type: ignore[misc,assignment]


class InspectorscanService(
    ServiceFactory[InspectorscanClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "inspector-scan"
    _SERVICE_PROP = "inspector_scan"
