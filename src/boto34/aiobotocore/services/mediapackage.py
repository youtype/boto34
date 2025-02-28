"""
Wrapper for aiobotocore MediaPackage service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediapackage/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_mediapackage.client import MediaPackageClient

from boto34.aiobotocore.service_factory import ServiceFactory


class MediaPackageService(ServiceFactory[MediaPackageClient]):
    """
    MediaPackage service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediapackage/)
    """
