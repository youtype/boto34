"""
Wrapper for boto3 Imagebuilder service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_imagebuilder/)

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
    # Returns type annotated boto3 Imagebuilder client
    imagebuilder_client = session.imagebuilder.client()
    imagebuilder_client: types_boto3_imagebuilder.client.ImagebuilderClient
    ```
"""

from __future__ import annotations

from types_boto3_imagebuilder.client import ImagebuilderClient

from boto34.boto3.service_factory import ServiceFactory


class ImagebuilderService(ServiceFactory[ImagebuilderClient]):
    SERVICE_NAME = "imagebuilder"
    _SERVICE_PROP = "imagebuilder"
