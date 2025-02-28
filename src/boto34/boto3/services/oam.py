"""
Wrapper for boto3 CloudWatchObservabilityAccessManager service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_oam/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_oam.client import CloudWatchObservabilityAccessManagerClient

from boto34.boto3.service_factory import ServiceFactory


class CloudWatchObservabilityAccessManagerService(
    ServiceFactory[CloudWatchObservabilityAccessManagerClient]
):
    """
    CloudWatchObservabilityAccessManager service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_oam/)
    """
