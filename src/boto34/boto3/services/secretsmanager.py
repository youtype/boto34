"""
Wrapper for boto3 SecretsManager service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_secretsmanager/)

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
    # Returns type annotated boto3 SecretsManager client
    secretsmanager_client = session.secretsmanager.client()
    secretsmanager_client: types_boto3_secretsmanager.client.SecretsManagerClient
    ```
"""

from __future__ import annotations

from types_boto3_secretsmanager.client import SecretsManagerClient

from boto34.boto3.service_factory import ServiceFactory


class SecretsManagerService(ServiceFactory[SecretsManagerClient]):
    SERVICE_NAME = "secretsmanager"
    _SERVICE_PROP = "secretsmanager"
