"""
Wrapper for aiobotocore Panorama service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_panorama/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_panorama.client import PanoramaClient

from boto34.aiobotocore.service_factory import ServiceFactory


class PanoramaService(ServiceFactory[PanoramaClient]):
    """
    Panorama service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_panorama/)
    """
