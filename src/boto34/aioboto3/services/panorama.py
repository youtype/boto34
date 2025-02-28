"""
Wrapper for aioboto3 Panorama service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_panorama/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_panorama.client import PanoramaClient

from boto34.aioboto3.service_factory import ServiceFactory


class PanoramaService(ServiceFactory[PanoramaClient]):
    """
    Panorama service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_panorama/)
    """
