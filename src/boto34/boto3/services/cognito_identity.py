"""
Wrapper for boto3 CognitoIdentity service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_identity/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_cognito_identity.client import CognitoIdentityClient

from boto34.boto3.service_factory import ServiceFactory


class CognitoIdentityService(ServiceFactory[CognitoIdentityClient]):
    """
    CognitoIdentity service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_identity/)
    """
