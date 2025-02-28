"""
Wrapper for boto3 WorkSpaces service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_workspaces/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_workspaces.client import WorkSpacesClient

from boto34.boto3.service_factory import ServiceFactory


class WorkSpacesService(ServiceFactory[WorkSpacesClient]):
    """
    WorkSpaces service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_workspaces/)
    """
