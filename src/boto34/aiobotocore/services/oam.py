"""
Wrapper for aiobotocore CloudWatchObservabilityAccessManager service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_oam/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_oam.client import CloudWatchObservabilityAccessManagerClient

from boto34.aiobotocore.service_factory import ServiceFactory


class CloudWatchObservabilityAccessManagerService(
    ServiceFactory[CloudWatchObservabilityAccessManagerClient]
):
    """
    CloudWatchObservabilityAccessManager service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_oam/)
    """
