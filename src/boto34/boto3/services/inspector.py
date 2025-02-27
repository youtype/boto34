"""
Wrapper for boto3 Inspector service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_inspector/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.boto3 import Session

    # Wrapper for boto3.Session constructor
    # Returns boto34.Session inherited from boto3.Session
    session = Session()
    session: boto34.boto3.session.Session

    # Type annotated boto3.Client
    # Uses the same arguments as boto3.client method
    # Returns type annotated boto3 Inspector client
    inspector_client = session.inspector.client()
    inspector_client: types_boto3_inspector.client.InspectorClient
    ```
"""

from __future__ import annotations

from types_boto3_inspector.client import InspectorClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_inspector.client import InspectorClient
except ImportError:
    InspectorClient = object  # type: ignore[misc,assignment]


class InspectorService(
    ServiceFactory[InspectorClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "inspector"
    _SERVICE_PROP = "inspector"
