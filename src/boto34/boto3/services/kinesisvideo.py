"""
Wrapper for boto3 KinesisVideo service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_kinesisvideo/)

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
    # Returns type annotated boto3 KinesisVideo client
    kinesisvideo_client = session.kinesisvideo.client()
    kinesisvideo_client: types_boto3_kinesisvideo.client.KinesisVideoClient
    ```
"""

from __future__ import annotations

from types_boto3_kinesisvideo.client import KinesisVideoClient

from boto34.boto3.service_factory import ServiceFactory


class KinesisVideoService(ServiceFactory[KinesisVideoClient]):
    SERVICE_NAME = "kinesisvideo"
    _SERVICE_PROP = "kinesisvideo"
