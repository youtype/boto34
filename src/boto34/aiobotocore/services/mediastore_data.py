"""
Wrapper for aiobotocore MediaStoreData service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediastore_data/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_mediastore_data.client import MediaStoreDataClient

from boto34.aiobotocore.service_factory import ServiceFactory


class MediaStoreDataService(ServiceFactory[MediaStoreDataClient]):
    """
    MediaStoreData service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediastore_data/)
    """
