"""
Wrapper for aiobotocore KinesisVideo service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisvideo/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_kinesisvideo.client import KinesisVideoClient

from boto34.aiobotocore.service_factory import ServiceFactory


class KinesisVideoService(ServiceFactory[KinesisVideoClient]):
    """
    KinesisVideo service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisvideo/)
    """
