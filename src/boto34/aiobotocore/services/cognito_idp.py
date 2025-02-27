"""
Wrapper for aiobotocore CognitoIdentityProvider service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cognito_idp/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore CognitoIdentityProvider client
    async with session.cognito_idp.create_client() as cognito_idp_client:
        cognito_idp_client: types_aiobotocore_cognito_idp.client.CognitoIdentityProviderClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_cognito_idp.client import CognitoIdentityProviderClient

from boto34.aiobotocore.service_factory import ServiceFactory


class CognitoIdentityProviderService(ServiceFactory[CognitoIdentityProviderClient]):
    SERVICE_NAME = "cognito-idp"
    _SERVICE_PROP = "cognito_idp"
