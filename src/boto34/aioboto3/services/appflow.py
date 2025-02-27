"""
Wrapper for aioboto3 Appflow service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_appflow/)

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
    # Returns type annotated aioboto3 Appflow client
    appflow_client = session.appflow.client()
    appflow_client: types_aiobotocore_appflow.client.AppflowClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_appflow.client import AppflowClient
except ImportError:
    AppflowClient = object  # type: ignore[misc,assignment]


class AppflowService(
    ServiceFactory[AppflowClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "appflow"
    _SERVICE_PROP = "appflow"
