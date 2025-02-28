"""
Wrapper for aioboto3 KinesisVideo service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_kinesisvideo/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_kinesisvideo.client import KinesisVideoClient

from boto34.aioboto3.service_factory import ServiceFactory


class KinesisVideoService(ServiceFactory[KinesisVideoClient]):
    """
    KinesisVideo service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_kinesisvideo/)
    """
