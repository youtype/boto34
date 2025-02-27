"""
Wrapper for aiobotocore BackupGateway service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup_gateway/)

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
    # Returns type annotated aiobotocore BackupGateway client
    async with session.backup_gateway.create_client() as backup_gateway_client:
        backup_gateway_client: types_aiobotocore_backup_gateway.client.BackupGatewayClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_backup_gateway.client import BackupGatewayClient

from boto34.aiobotocore.service_factory import ServiceFactory


class BackupGatewayService(ServiceFactory[BackupGatewayClient]):
    SERVICE_NAME = "backup-gateway"
    _SERVICE_PROP = "backup_gateway"
