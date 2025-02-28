"""
Wrapper for aiobotocore AppMesh service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appmesh/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_appmesh.client import AppMeshClient

from boto34.aiobotocore.service_factory import ServiceFactory


class AppMeshService(ServiceFactory[AppMeshClient]):
    """
    AppMesh service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appmesh/)
    """
