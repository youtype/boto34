"""
Wrapper for aiobotocore MediaConnect service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_mediaconnect.client import MediaConnectClient

from boto34.aiobotocore.service_factory import ServiceFactory


class MediaConnectService(ServiceFactory[MediaConnectClient]):
    """
    MediaConnect service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/)
    """
