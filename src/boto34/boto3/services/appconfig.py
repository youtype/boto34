"""
Wrapper for boto3 AppConfig service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_appconfig/)

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
    # Returns type annotated boto3 AppConfig client
    appconfig_client = session.appconfig.client()
    appconfig_client: types_boto3_appconfig.client.AppConfigClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_appconfig.client import AppConfigClient
except ImportError:
    AppConfigClient = object  # type: ignore[misc,assignment]


class AppConfigService(
    ServiceFactory[AppConfigClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "appconfig"
    _SERVICE_PROP = "appconfig"
