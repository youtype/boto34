"""
Wrapper for boto3 CognitoIdentity service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_identity/)

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
    # Returns type annotated boto3 CognitoIdentity client
    cognito_identity_client = session.cognito_identity.client()
    cognito_identity_client: types_boto3_cognito_identity.client.CognitoIdentityClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_cognito_identity.client import CognitoIdentityClient
except ImportError:
    CognitoIdentityClient = object  # type: ignore[misc,assignment]


class CognitoIdentityService(
    ServiceFactory[CognitoIdentityClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "cognito-identity"
    _SERVICE_PROP = "cognito_identity"
