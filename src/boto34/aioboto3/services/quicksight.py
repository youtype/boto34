"""
Wrapper for aioboto3 QuickSight service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_quicksight/)

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
    # Returns type annotated aioboto3 QuickSight client
    quicksight_client = session.quicksight.client()
    quicksight_client: types_aiobotocore_quicksight.client.QuickSightClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_quicksight.client import QuickSightClient
except ImportError:
    QuickSightClient = object  # type: ignore[misc,assignment]


class QuickSightService(
    ServiceFactory[QuickSightClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "quicksight"
    _SERVICE_PROP = "quicksight"
