"""
Wrapper for boto3 BackupGateway service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_backup_gateway/)

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
    # Returns type annotated boto3 BackupGateway client
    backup_gateway_client = session.backup_gateway.client()
    backup_gateway_client: types_boto3_backup_gateway.client.BackupGatewayClient
    ```
"""

from __future__ import annotations

from types_boto3_backup_gateway.client import BackupGatewayClient

from boto34.boto3.service_factory import ServiceFactory


class BackupGatewayService(ServiceFactory[BackupGatewayClient]):
    SERVICE_NAME = "backup-gateway"
    _SERVICE_PROP = "backup_gateway"
