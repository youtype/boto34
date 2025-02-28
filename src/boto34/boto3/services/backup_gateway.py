"""
Wrapper for boto3 BackupGateway service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_backup_gateway/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_backup_gateway.client import BackupGatewayClient

from boto34.boto3.service_factory import ServiceFactory


class BackupGatewayService(ServiceFactory[BackupGatewayClient]):
    """
    BackupGateway service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_backup_gateway/)
    """
