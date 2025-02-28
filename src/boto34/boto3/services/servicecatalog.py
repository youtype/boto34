"""
Wrapper for boto3 ServiceCatalog service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_servicecatalog/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_servicecatalog.client import ServiceCatalogClient

from boto34.boto3.service_factory import ServiceFactory


class ServiceCatalogService(ServiceFactory[ServiceCatalogClient]):
    """
    ServiceCatalog service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_servicecatalog/)
    """
