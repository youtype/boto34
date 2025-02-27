"""
Wrapper for aioboto3 BackupGateway service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_backup_gateway/)

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
    # Returns type annotated aioboto3 BackupGateway client
    backup_gateway_client = session.backup_gateway.client()
    backup_gateway_client: types_aiobotocore_backup_gateway.client.BackupGatewayClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_backup_gateway.client import BackupGatewayClient
except ImportError:
    BackupGatewayClient = object  # type: ignore[misc,assignment]


class BackupGatewayService(
    ServiceFactory[BackupGatewayClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "backup-gateway"
    _SERVICE_PROP = "backup_gateway"
