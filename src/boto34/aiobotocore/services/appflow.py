"""
Wrapper for aiobotocore Appflow service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appflow/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore Appflow client
    async with session.appflow.create_client() as appflow_client:
        appflow_client: types_aiobotocore_appflow.client.AppflowClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_appflow.client import AppflowClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_appflow.client import AppflowClient
except ImportError:
    AppflowClient = object  # type: ignore[misc,assignment]


class AppflowService(
    ServiceFactory[AppflowClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "appflow"
    _SERVICE_PROP = "appflow"
