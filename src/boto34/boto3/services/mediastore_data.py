"""
Wrapper for boto3 MediaStoreData service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_mediastore_data/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.boto3 import Session

    # Wrapper for boto3.Session constructor
    # Returns boto34.Session inherited from boto3.Session
    session = Session()
    session: boto34.boto3.session.Session

    # Type annotated boto3.Client
    # Uses the same arguments as boto3.client method
    # Returns type annotated boto3 MediaStoreData client
    mediastore_data_client = session.mediastore_data.client()
    mediastore_data_client: types_boto3_mediastore_data.client.MediaStoreDataClient
    ```
"""

from __future__ import annotations

from types_boto3_mediastore_data.client import MediaStoreDataClient

from boto34.boto3.service_factory import ServiceFactory


class MediaStoreDataService(ServiceFactory[MediaStoreDataClient]):
    SERVICE_NAME = "mediastore-data"
    _SERVICE_PROP = "mediastore_data"
