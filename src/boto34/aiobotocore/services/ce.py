"""
Wrapper for aiobotocore CostExplorer service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ce/)

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
    # Returns type annotated aiobotocore CostExplorer client
    async with session.ce.create_client() as ce_client:
        ce_client: types_aiobotocore_ce.client.CostExplorerClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_ce.client import CostExplorerClient
except ImportError:
    CostExplorerClient = object  # type: ignore[misc,assignment]


class CostExplorerService(
    ServiceFactory[CostExplorerClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "ce"
    _SERVICE_PROP = "ce"
