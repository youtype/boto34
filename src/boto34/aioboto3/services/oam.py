"""
Wrapper for aioboto3 CloudWatchObservabilityAccessManager service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_oam/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_oam.client import CloudWatchObservabilityAccessManagerClient

from boto34.aioboto3.service_factory import ServiceFactory


class CloudWatchObservabilityAccessManagerService(
    ServiceFactory[CloudWatchObservabilityAccessManagerClient]
):
    """
    CloudWatchObservabilityAccessManager service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_oam/)
    """
