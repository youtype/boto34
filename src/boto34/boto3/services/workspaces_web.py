"""
Wrapper for boto3 WorkSpacesWeb service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_workspaces_web/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_workspaces_web.client import WorkSpacesWebClient

from boto34.boto3.service_factory import ServiceFactory


class WorkSpacesWebService(ServiceFactory[WorkSpacesWebClient]):
    """
    WorkSpacesWeb service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_workspaces_web/)
    """
