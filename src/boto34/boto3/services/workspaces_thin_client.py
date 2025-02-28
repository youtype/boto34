"""
Wrapper for boto3 WorkSpacesThinClient service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_workspaces_thin_client/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_workspaces_thin_client.client import WorkSpacesThinClientClient

from boto34.boto3.service_factory import ServiceFactory


class WorkSpacesThinClientService(ServiceFactory[WorkSpacesThinClientClient]):
    """
    WorkSpacesThinClient service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_workspaces_thin_client/)
    """
