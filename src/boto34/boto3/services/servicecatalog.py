"""
Wrapper for boto3 ServiceCatalog service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_servicecatalog/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.boto3 import Session

    # Wrapper for boto3.Session constructor
    # Returns boto34.Session inherited from boto3.Session
    session = Session()
    session: boto34.boto3.session.Session

    # Type annotated boto3.Client
    # Uses the same arguments as boto3.client method
    # Returns type annotated boto3 ServiceCatalog client
    servicecatalog_client = session.servicecatalog.client()
    servicecatalog_client: types_boto3_servicecatalog.client.ServiceCatalogClient
    ```
"""

from __future__ import annotations

from types_boto3_servicecatalog.client import ServiceCatalogClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_servicecatalog.client import ServiceCatalogClient
except ImportError:
    ServiceCatalogClient = object  # type: ignore[misc,assignment]


class ServiceCatalogService(
    ServiceFactory[ServiceCatalogClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "servicecatalog"
    _SERVICE_PROP = "servicecatalog"
