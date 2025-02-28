"""
Wrapper for aiobotocore WorkSpacesThinClient service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_thin_client/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_workspaces_thin_client.client import WorkSpacesThinClientClient

from boto34.aiobotocore.service_factory import ServiceFactory


class WorkSpacesThinClientService(ServiceFactory[WorkSpacesThinClientClient]):
    """
    WorkSpacesThinClient service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_thin_client/)
    """
