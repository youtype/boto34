"""
Wrapper for boto3 MediaTailor service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_mediatailor/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_mediatailor.client import MediaTailorClient

from boto34.boto3.service_factory import ServiceFactory


class MediaTailorService(ServiceFactory[MediaTailorClient]):
    """
    MediaTailor service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_mediatailor/)
    """
