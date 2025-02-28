"""
Wrapper for boto3 ResourceGroupsTaggingAPI service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_resourcegroupstaggingapi/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_resourcegroupstaggingapi.client import ResourceGroupsTaggingAPIClient

from boto34.boto3.service_factory import ServiceFactory


class ResourceGroupsTaggingAPIService(ServiceFactory[ResourceGroupsTaggingAPIClient]):
    """
    ResourceGroupsTaggingAPI service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_resourcegroupstaggingapi/)
    """
