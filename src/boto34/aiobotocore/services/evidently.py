"""
Wrapper for aiobotocore CloudWatchEvidently service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_evidently/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_evidently.client import CloudWatchEvidentlyClient

from boto34.aiobotocore.service_factory import ServiceFactory


class CloudWatchEvidentlyService(ServiceFactory[CloudWatchEvidentlyClient]):
    """
    CloudWatchEvidently service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_evidently/)
    """
