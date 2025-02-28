"""
Wrapper for aiobotocore WorkSpacesWeb service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_workspaces_web.client import WorkSpacesWebClient

from boto34.aiobotocore.service_factory import ServiceFactory


class WorkSpacesWebService(ServiceFactory[WorkSpacesWebClient]):
    """
    WorkSpacesWeb service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/)
    """
