"""
Wrapper for aioboto3 DatabaseMigrationService service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_dms/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_dms.client import DatabaseMigrationServiceClient

from boto34.aioboto3.service_factory import ServiceFactory


class DatabaseMigrationServiceService(ServiceFactory[DatabaseMigrationServiceClient]):
    """
    DatabaseMigrationService service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_dms/)
    """
