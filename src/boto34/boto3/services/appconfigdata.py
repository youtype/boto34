"""
Wrapper for boto3 AppConfigData service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_appconfigdata/)

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
    # Returns type annotated boto3 AppConfigData client
    appconfigdata_client = session.appconfigdata.client()
    appconfigdata_client: types_boto3_appconfigdata.client.AppConfigDataClient
    ```
"""

from __future__ import annotations

from types_boto3_appconfigdata.client import AppConfigDataClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_appconfigdata.client import AppConfigDataClient
except ImportError:
    AppConfigDataClient = object  # type: ignore[misc,assignment]


class AppConfigDataService(
    ServiceFactory[AppConfigDataClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "appconfigdata"
    _SERVICE_PROP = "appconfigdata"
