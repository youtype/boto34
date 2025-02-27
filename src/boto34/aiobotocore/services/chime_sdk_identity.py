"""
Wrapper for aiobotocore ChimeSDKIdentity service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_chime_sdk_identity/)

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
    # Returns type annotated aiobotocore ChimeSDKIdentity client
    async with session.chime_sdk_identity.create_client() as chime_sdk_identity_client:
        chime_sdk_identity_client: types_aiobotocore_chime_sdk_identity.client.ChimeSDKIdentityClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_chime_sdk_identity.client import ChimeSDKIdentityClient
except ImportError:
    ChimeSDKIdentityClient = object  # type: ignore[misc,assignment]


class ChimeSDKIdentityService(
    ServiceFactory[ChimeSDKIdentityClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "chime-sdk-identity"
    _SERVICE_PROP = "chime_sdk_identity"
