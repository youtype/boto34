"""
Wrapper for boto3 AppIntegrationsService service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_appintegrations/)

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
    # Returns type annotated boto3 AppIntegrationsService client
    appintegrations_client = session.appintegrations.client()
    appintegrations_client: types_boto3_appintegrations.client.AppIntegrationsServiceClient
    ```
"""

from __future__ import annotations

from types_boto3_appintegrations.client import AppIntegrationsServiceClient

from boto34.boto3.service_factory import ServiceFactory


class AppIntegrationsServiceService(ServiceFactory[AppIntegrationsServiceClient]):
    SERVICE_NAME = "appintegrations"
    _SERVICE_PROP = "appintegrations"
