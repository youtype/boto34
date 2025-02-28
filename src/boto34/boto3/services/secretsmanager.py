"""
Wrapper for boto3 SecretsManager service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_secretsmanager/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_secretsmanager.client import SecretsManagerClient

from boto34.boto3.service_factory import ServiceFactory


class SecretsManagerService(ServiceFactory[SecretsManagerClient]):
    """
    SecretsManager service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_secretsmanager/)
    """
