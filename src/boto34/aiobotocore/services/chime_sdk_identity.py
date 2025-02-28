"""
Wrapper for aiobotocore ChimeSDKIdentity service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_chime_sdk_identity/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_chime_sdk_identity.client import ChimeSDKIdentityClient

from boto34.aiobotocore.service_factory import ServiceFactory


class ChimeSDKIdentityService(ServiceFactory[ChimeSDKIdentityClient]):
    """
    ChimeSDKIdentity service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_chime_sdk_identity/)
    """
