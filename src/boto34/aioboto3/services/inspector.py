"""
Wrapper for aioboto3 Inspector service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_inspector/)

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
    # Returns type annotated aioboto3 Inspector client
    inspector_client = session.inspector.client()
    inspector_client: types_aiobotocore_inspector.client.InspectorClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_inspector.client import InspectorClient
except ImportError:
    InspectorClient = object  # type: ignore[misc,assignment]


class InspectorService(
    ServiceFactory[InspectorClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "inspector"
    _SERVICE_PROP = "inspector"
