"""
Wrapper for boto3 CloudDirectory service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_clouddirectory/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_clouddirectory.client import CloudDirectoryClient

from boto34.boto3.service_factory import ServiceFactory


class CloudDirectoryService(ServiceFactory[CloudDirectoryClient]):
    """
    CloudDirectory service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_clouddirectory/)
    """
