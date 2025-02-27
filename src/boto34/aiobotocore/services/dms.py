"""
Wrapper for aiobotocore DatabaseMigrationService service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/)

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
    # Returns type annotated aiobotocore DatabaseMigrationService client
    async with session.dms.create_client() as dms_client:
        dms_client: types_aiobotocore_dms.client.DatabaseMigrationServiceClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_dms.client import DatabaseMigrationServiceClient
except ImportError:
    DatabaseMigrationServiceClient = object  # type: ignore[misc,assignment]


class DatabaseMigrationServiceService(
    ServiceFactory[DatabaseMigrationServiceClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "dms"
    _SERVICE_PROP = "dms"
