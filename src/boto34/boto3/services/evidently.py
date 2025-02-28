"""
Wrapper for boto3 CloudWatchEvidently service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_evidently/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_evidently.client import CloudWatchEvidentlyClient

from boto34.boto3.service_factory import ServiceFactory


class CloudWatchEvidentlyService(ServiceFactory[CloudWatchEvidentlyClient]):
    """
    CloudWatchEvidently service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_evidently/)
    """
