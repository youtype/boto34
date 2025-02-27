"""
Wrapper for boto3 MainframeModernizationApplicationTesting service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_apptest/)

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
    # Returns type annotated boto3 MainframeModernizationApplicationTesting client
    apptest_client = session.apptest.client()
    apptest_client: types_boto3_apptest.client.MainframeModernizationApplicationTestingClient
    ```
"""

from __future__ import annotations

from types_boto3_apptest.client import MainframeModernizationApplicationTestingClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_apptest.client import MainframeModernizationApplicationTestingClient
except ImportError:
    MainframeModernizationApplicationTestingClient = object  # type: ignore[misc,assignment]


class MainframeModernizationApplicationTestingService(
    ServiceFactory[MainframeModernizationApplicationTestingClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "apptest"
    _SERVICE_PROP = "apptest"
