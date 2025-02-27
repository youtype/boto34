"""
Wrapper for aioboto3 AppIntegrationsService service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_appintegrations/)

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
    # Returns type annotated aioboto3 AppIntegrationsService client
    appintegrations_client = session.appintegrations.client()
    appintegrations_client: types_aiobotocore_appintegrations.client.AppIntegrationsServiceClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_appintegrations.client import AppIntegrationsServiceClient

from boto34.aioboto3.service_factory import ServiceFactory


class AppIntegrationsServiceService(ServiceFactory[AppIntegrationsServiceClient]):
    SERVICE_NAME = "appintegrations"
    _SERVICE_PROP = "appintegrations"
