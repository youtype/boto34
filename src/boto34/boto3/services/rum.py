"""
Wrapper for boto3 CloudWatchRUM service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_rum/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_rum.client import CloudWatchRUMClient

from boto34.boto3.service_factory import ServiceFactory


class CloudWatchRUMService(ServiceFactory[CloudWatchRUMClient]):
    """
    CloudWatchRUM service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_rum/)
    """
