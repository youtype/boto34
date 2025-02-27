"""
Wrapper for boto3 DatabaseMigrationService service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_dms/)

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
    # Returns type annotated boto3 DatabaseMigrationService client
    dms_client = session.dms.client()
    dms_client: types_boto3_dms.client.DatabaseMigrationServiceClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_dms.client import DatabaseMigrationServiceClient
except ImportError:
    DatabaseMigrationServiceClient = object  # type: ignore[misc,assignment]


class DatabaseMigrationServiceService(
    ServiceFactory[DatabaseMigrationServiceClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "dms"
    _SERVICE_PROP = "dms"
