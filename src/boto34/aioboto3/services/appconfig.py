"""
Wrapper for aioboto3 AppConfig service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_appconfig/)

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
    # Returns type annotated aioboto3 AppConfig client
    appconfig_client = session.appconfig.client()
    appconfig_client: types_aiobotocore_appconfig.client.AppConfigClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_appconfig.client import AppConfigClient

from boto34.aioboto3.service_factory import ServiceFactory


class AppConfigService(ServiceFactory[AppConfigClient]):
    SERVICE_NAME = "appconfig"
    _SERVICE_PROP = "appconfig"
