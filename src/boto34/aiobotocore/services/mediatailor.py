"""
Wrapper for aiobotocore MediaTailor service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_mediatailor.client import MediaTailorClient

from boto34.aiobotocore.service_factory import ServiceFactory


class MediaTailorService(ServiceFactory[MediaTailorClient]):
    """
    MediaTailor service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/)
    """
