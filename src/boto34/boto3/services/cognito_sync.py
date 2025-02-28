"""
Wrapper for boto3 CognitoSync service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_sync/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_cognito_sync.client import CognitoSyncClient

from boto34.boto3.service_factory import ServiceFactory


class CognitoSyncService(ServiceFactory[CognitoSyncClient]):
    """
    CognitoSync service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_sync/)
    """
