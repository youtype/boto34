"""
Wrapper for aioboto3 CognitoIdentity service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_cognito_identity/)

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
    # Returns type annotated aioboto3 CognitoIdentity client
    cognito_identity_client = session.cognito_identity.client()
    cognito_identity_client: types_aiobotocore_cognito_identity.client.CognitoIdentityClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_cognito_identity.client import CognitoIdentityClient

from boto34.aioboto3.service_factory import ServiceFactory


class CognitoIdentityService(ServiceFactory[CognitoIdentityClient]):
    SERVICE_NAME = "cognito-identity"
    _SERVICE_PROP = "cognito_identity"
