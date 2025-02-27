"""
Wrapper for boto3 MediaStore service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_mediastore/)

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
    # Returns type annotated boto3 MediaStore client
    mediastore_client = session.mediastore.client()
    mediastore_client: types_boto3_mediastore.client.MediaStoreClient
    ```
"""

from __future__ import annotations

from types_boto3_mediastore.client import MediaStoreClient

from boto34.boto3.service_factory import ServiceFactory


class MediaStoreService(ServiceFactory[MediaStoreClient]):
    SERVICE_NAME = "mediastore"
    _SERVICE_PROP = "mediastore"
