"""
Wrapper for aioboto3 CognitoIdentityProvider service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_cognito_idp/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_cognito_idp.client import CognitoIdentityProviderClient

from boto34.aioboto3.service_factory import ServiceFactory


class CognitoIdentityProviderService(ServiceFactory[CognitoIdentityProviderClient]):
    """
    CognitoIdentityProvider service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_cognito_idp/)
    """
