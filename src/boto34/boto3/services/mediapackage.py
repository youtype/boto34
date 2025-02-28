"""
Wrapper for boto3 MediaPackage service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_mediapackage/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_mediapackage.client import MediaPackageClient

from boto34.boto3.service_factory import ServiceFactory


class MediaPackageService(ServiceFactory[MediaPackageClient]):
    """
    MediaPackage service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_mediapackage/)
    """
