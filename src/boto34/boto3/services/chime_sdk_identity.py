"""
Wrapper for boto3 ChimeSDKIdentity service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_chime_sdk_identity/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_chime_sdk_identity.client import ChimeSDKIdentityClient

from boto34.boto3.service_factory import ServiceFactory


class ChimeSDKIdentityService(ServiceFactory[ChimeSDKIdentityClient]):
    """
    ChimeSDKIdentity service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_chime_sdk_identity/)
    """
