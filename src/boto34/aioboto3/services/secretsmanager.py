"""
Wrapper for aioboto3 SecretsManager service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_secretsmanager/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_secretsmanager.client import SecretsManagerClient

from boto34.aioboto3.service_factory import ServiceFactory


class SecretsManagerService(ServiceFactory[SecretsManagerClient]):
    """
    SecretsManager service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_secretsmanager/)
    """
