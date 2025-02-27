"""
Wrapper for aioboto3 DatabaseMigrationService service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_dms/)

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
    # Returns type annotated aioboto3 DatabaseMigrationService client
    dms_client = session.dms.client()
    dms_client: types_aiobotocore_dms.client.DatabaseMigrationServiceClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_dms.client import DatabaseMigrationServiceClient

from boto34.aioboto3.service_factory import ServiceFactory


class DatabaseMigrationServiceService(ServiceFactory[DatabaseMigrationServiceClient]):
    SERVICE_NAME = "dms"
    _SERVICE_PROP = "dms"
