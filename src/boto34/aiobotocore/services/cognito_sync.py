"""
Wrapper for aiobotocore CognitoSync service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cognito_sync/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_cognito_sync.client import CognitoSyncClient

from boto34.aiobotocore.service_factory import ServiceFactory


class CognitoSyncService(ServiceFactory[CognitoSyncClient]):
    """
    CognitoSync service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cognito_sync/)
    """
