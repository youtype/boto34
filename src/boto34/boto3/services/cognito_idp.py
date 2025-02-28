"""
Wrapper for boto3 CognitoIdentityProvider service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_cognito_idp.client import CognitoIdentityProviderClient

from boto34.boto3.service_factory import ServiceFactory


class CognitoIdentityProviderService(ServiceFactory[CognitoIdentityProviderClient]):
    """
    CognitoIdentityProvider service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/)
    """
