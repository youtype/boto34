"""
Wrapper for aioboto3 Inspectorscan service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_inspector_scan/)

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
    # Returns type annotated aioboto3 Inspectorscan client
    inspector_scan_client = session.inspector_scan.client()
    inspector_scan_client: types_aiobotocore_inspector_scan.client.InspectorscanClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_inspector_scan.client import InspectorscanClient

from boto34.aioboto3.service_factory import ServiceFactory


class InspectorscanService(ServiceFactory[InspectorscanClient]):
    SERVICE_NAME = "inspector-scan"
    _SERVICE_PROP = "inspector_scan"
