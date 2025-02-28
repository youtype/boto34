"""
Wrapper for boto3 DirectoryService service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_ds/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_ds.client import DirectoryServiceClient

from boto34.boto3.service_factory import ServiceFactory


class DirectoryServiceService(ServiceFactory[DirectoryServiceClient]):
    """
    DirectoryService service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_ds/)
    """
