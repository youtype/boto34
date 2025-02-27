"""
Wrapper for boto3 AppRegistry service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_servicecatalog_appregistry/)

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
    # Returns type annotated boto3 AppRegistry client
    servicecatalog_appregistry_client = session.servicecatalog_appregistry.client()
    servicecatalog_appregistry_client: types_boto3_servicecatalog_appregistry.client.AppRegistryClient
    ```
"""

from __future__ import annotations

from types_boto3_servicecatalog_appregistry.client import AppRegistryClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_servicecatalog_appregistry.client import AppRegistryClient
except ImportError:
    AppRegistryClient = object  # type: ignore[misc,assignment]


class AppRegistryService(
    ServiceFactory[AppRegistryClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "servicecatalog-appregistry"
    _SERVICE_PROP = "servicecatalog_appregistry"
