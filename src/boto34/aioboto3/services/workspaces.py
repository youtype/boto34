"""
Wrapper for aioboto3 WorkSpaces service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_workspaces/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_workspaces.client import WorkSpacesClient

from boto34.aioboto3.service_factory import ServiceFactory


class WorkSpacesService(ServiceFactory[WorkSpacesClient]):
    """
    WorkSpaces service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_workspaces/)
    """
