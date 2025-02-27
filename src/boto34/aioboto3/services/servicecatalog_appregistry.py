"""
Wrapper for aioboto3 AppRegistry service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_servicecatalog_appregistry/)

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
    # Returns type annotated aioboto3 AppRegistry client
    servicecatalog_appregistry_client = session.servicecatalog_appregistry.client()
    servicecatalog_appregistry_client: (
        types_aiobotocore_servicecatalog_appregistry.client.AppRegistryClient
    )
    ```
"""

from __future__ import annotations

from types_aiobotocore_servicecatalog_appregistry.client import AppRegistryClient

from boto34.aioboto3.service_factory import ServiceFactory


class AppRegistryService(ServiceFactory[AppRegistryClient]):
    SERVICE_NAME = "servicecatalog-appregistry"
    _SERVICE_PROP = "servicecatalog_appregistry"
