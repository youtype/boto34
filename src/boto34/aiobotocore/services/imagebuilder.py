"""
Wrapper for aiobotocore Imagebuilder service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_imagebuilder/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_imagebuilder.client import ImagebuilderClient

from boto34.aiobotocore.service_factory import ServiceFactory


class ImagebuilderService(ServiceFactory[ImagebuilderClient]):
    """
    Imagebuilder service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_imagebuilder/)
    """
