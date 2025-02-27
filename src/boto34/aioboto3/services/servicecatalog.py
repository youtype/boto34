"""
Wrapper for aioboto3 ServiceCatalog service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_servicecatalog/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aioboto3 import Session

    # Wrapper for aioboto3.Session constructor
    # Returns boto34.Session inherited from aioboto3.Session
    session = Session()
    session: boto34.aioboto3.session.Session

    # Type annotated aioboto3.Client
    # Uses the same arguments as aioboto3.client method
    # Returns type annotated aioboto3 ServiceCatalog client
    servicecatalog_client = session.servicecatalog.client()
    servicecatalog_client: types_aiobotocore_servicecatalog.client.ServiceCatalogClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_servicecatalog.client import ServiceCatalogClient

from boto34.aioboto3.service_factory import ServiceFactory


class ServiceCatalogService(ServiceFactory[ServiceCatalogClient]):
    SERVICE_NAME = "servicecatalog"
    _SERVICE_PROP = "servicecatalog"
