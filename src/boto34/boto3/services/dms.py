"""
Wrapper for boto3 DatabaseMigrationService service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_dms/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_dms.client import DatabaseMigrationServiceClient

from boto34.boto3.service_factory import ServiceFactory


class DatabaseMigrationServiceService(ServiceFactory[DatabaseMigrationServiceClient]):
    """
    DatabaseMigrationService service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_dms/)
    """
