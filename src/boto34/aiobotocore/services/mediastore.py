"""
Wrapper for aiobotocore MediaStore service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediastore/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_mediastore.client import MediaStoreClient

from boto34.aiobotocore.service_factory import ServiceFactory


class MediaStoreService(ServiceFactory[MediaStoreClient]):
    """
    MediaStore service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediastore/)
    """
