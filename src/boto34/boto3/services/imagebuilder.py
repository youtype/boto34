"""
Wrapper for boto3 Imagebuilder service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_imagebuilder/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_imagebuilder.client import ImagebuilderClient

from boto34.boto3.service_factory import ServiceFactory


class ImagebuilderService(ServiceFactory[ImagebuilderClient]):
    """
    Imagebuilder service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_imagebuilder/)
    """
