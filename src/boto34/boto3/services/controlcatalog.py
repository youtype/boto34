"""
Wrapper for boto3 ControlCatalog service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_controlcatalog/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_controlcatalog.client import ControlCatalogClient

from boto34.boto3.service_factory import ServiceFactory


class ControlCatalogService(ServiceFactory[ControlCatalogClient]):
    """
    ControlCatalog service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_controlcatalog/)
    """
