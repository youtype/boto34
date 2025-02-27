"""
Wrapper for aioboto3 CognitoIdentityProvider service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_cognito_idp/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aioboto3 import Session

    # Wrapper for aioboto3.Session constructor
    # Returns boto34.Session inherited from aioboto3.Session
    session = Session()
    session: boto34.aioboto3.session.Session

    # Type annotated aioboto3.Client
    # Uses the same arguments as aioboto3.client method
    # Returns type annotated aioboto3 CognitoIdentityProvider client
    cognito_idp_client = session.cognito_idp.client()
    cognito_idp_client: types_aiobotocore_cognito_idp.client.CognitoIdentityProviderClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_cognito_idp.client import CognitoIdentityProviderClient

from boto34.aioboto3.service_factory import ServiceFactory


class CognitoIdentityProviderService(ServiceFactory[CognitoIdentityProviderClient]):
    SERVICE_NAME = "cognito-idp"
    _SERVICE_PROP = "cognito_idp"
