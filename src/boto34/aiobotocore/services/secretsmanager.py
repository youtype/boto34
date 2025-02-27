"""
Wrapper for aiobotocore SecretsManager service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_secretsmanager/)

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
    # Returns type annotated aiobotocore SecretsManager client
    async with session.secretsmanager.create_client() as secretsmanager_client:
        secretsmanager_client: types_aiobotocore_secretsmanager.client.SecretsManagerClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_secretsmanager.client import SecretsManagerClient

from boto34.aiobotocore.service_factory import ServiceFactory


class SecretsManagerService(ServiceFactory[SecretsManagerClient]):
    SERVICE_NAME = "secretsmanager"
    _SERVICE_PROP = "secretsmanager"
