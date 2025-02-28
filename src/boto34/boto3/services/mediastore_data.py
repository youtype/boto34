"""
Wrapper for boto3 MediaStoreData service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_mediastore_data/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_mediastore_data.client import MediaStoreDataClient

from boto34.boto3.service_factory import ServiceFactory


class MediaStoreDataService(ServiceFactory[MediaStoreDataClient]):
    """
    MediaStoreData service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_mediastore_data/)
    """
