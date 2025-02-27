"""
Wrapper for boto3 CognitoIdentityProvider service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/)

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
    # Returns type annotated boto3 CognitoIdentityProvider client
    cognito_idp_client = session.cognito_idp.client()
    cognito_idp_client: types_boto3_cognito_idp.client.CognitoIdentityProviderClient
    ```
"""

from __future__ import annotations

from types_boto3_cognito_idp.client import CognitoIdentityProviderClient

from boto34.boto3.service_factory import ServiceFactory


class CognitoIdentityProviderService(ServiceFactory[CognitoIdentityProviderClient]):
    SERVICE_NAME = "cognito-idp"
    _SERVICE_PROP = "cognito_idp"
