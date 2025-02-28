"""
Wrapper for aioboto3 MediaConnect service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_mediaconnect/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_mediaconnect.client import MediaConnectClient

from boto34.aioboto3.service_factory import ServiceFactory


class MediaConnectService(ServiceFactory[MediaConnectClient]):
    """
    MediaConnect service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_mediaconnect/)
    """
