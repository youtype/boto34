"""
Wrapper for boto3 Inspectorscan service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_inspector_scan/)

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
    # Returns type annotated boto3 Inspectorscan client
    inspector_scan_client = session.inspector_scan.client()
    inspector_scan_client: types_boto3_inspector_scan.client.InspectorscanClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_inspector_scan.client import InspectorscanClient
except ImportError:
    InspectorscanClient = object  # type: ignore[misc,assignment]


class InspectorscanService(
    ServiceFactory[InspectorscanClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "inspector-scan"
    _SERVICE_PROP = "inspector_scan"
