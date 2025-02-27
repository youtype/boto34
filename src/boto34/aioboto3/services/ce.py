"""
Wrapper for aioboto3 CostExplorer service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_ce/)

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
    # Returns type annotated aioboto3 CostExplorer client
    ce_client = session.ce.client()
    ce_client: types_aiobotocore_ce.client.CostExplorerClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_ce.client import CostExplorerClient
except ImportError:
    CostExplorerClient = object  # type: ignore[misc,assignment]


class CostExplorerService(
    ServiceFactory[CostExplorerClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "ce"
    _SERVICE_PROP = "ce"
