"""
Wrapper for boto3 AppMesh service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_appmesh/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_appmesh.client import AppMeshClient

from boto34.boto3.service_factory import ServiceFactory


class AppMeshService(ServiceFactory[AppMeshClient]):
    """
    AppMesh service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_appmesh/)
    """
