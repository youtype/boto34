"""
Wrapper for boto3 CognitoSync service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_sync/)

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
    # Returns type annotated boto3 CognitoSync client
    cognito_sync_client = session.cognito_sync.client()
    cognito_sync_client: types_boto3_cognito_sync.client.CognitoSyncClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_cognito_sync.client import CognitoSyncClient
except ImportError:
    CognitoSyncClient = object  # type: ignore[misc,assignment]


class CognitoSyncService(
    ServiceFactory[CognitoSyncClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "cognito-sync"
    _SERVICE_PROP = "cognito_sync"
