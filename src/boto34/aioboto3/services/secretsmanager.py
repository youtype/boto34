"""
Wrapper for aioboto3 SecretsManager service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_secretsmanager/)

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
    # Returns type annotated aioboto3 SecretsManager client
    secretsmanager_client = session.secretsmanager.client()
    secretsmanager_client: types_aiobotocore_secretsmanager.client.SecretsManagerClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_secretsmanager.client import SecretsManagerClient

from boto34.aioboto3.service_factory import ServiceFactory


class SecretsManagerService(ServiceFactory[SecretsManagerClient]):
    SERVICE_NAME = "secretsmanager"
    _SERVICE_PROP = "secretsmanager"
