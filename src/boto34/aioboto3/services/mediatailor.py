"""
Wrapper for aioboto3 MediaTailor service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_mediatailor/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_mediatailor.client import MediaTailorClient

from boto34.aioboto3.service_factory import ServiceFactory


class MediaTailorService(ServiceFactory[MediaTailorClient]):
    """
    MediaTailor service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_mediatailor/)
    """
