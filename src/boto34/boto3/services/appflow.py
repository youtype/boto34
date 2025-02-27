"""
Wrapper for boto3 Appflow service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_appflow/)

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
    # Returns type annotated boto3 Appflow client
    appflow_client = session.appflow.client()
    appflow_client: types_boto3_appflow.client.AppflowClient
    ```
"""

from __future__ import annotations

from types_boto3_appflow.client import AppflowClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_appflow.client import AppflowClient
except ImportError:
    AppflowClient = object  # type: ignore[misc,assignment]


class AppflowService(
    ServiceFactory[AppflowClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "appflow"
    _SERVICE_PROP = "appflow"
