"""
Wrapper for boto3 ResourceExplorer service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_resource_explorer_2/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_resource_explorer_2.client import ResourceExplorerClient

from boto34.boto3.service_factory import ServiceFactory


class ResourceExplorerService(ServiceFactory[ResourceExplorerClient]):
    """
    ResourceExplorer service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_resource_explorer_2/)
    """
