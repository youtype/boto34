"""
Wrapper for aioboto3 MainframeModernizationApplicationTesting service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_apptest/)

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
    # Returns type annotated aioboto3 MainframeModernizationApplicationTesting client
    apptest_client = session.apptest.client()
    apptest_client: types_aiobotocore_apptest.client.MainframeModernizationApplicationTestingClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_apptest.client import MainframeModernizationApplicationTestingClient

from boto34.aioboto3.service_factory import ServiceFactory


class MainframeModernizationApplicationTestingService(
    ServiceFactory[MainframeModernizationApplicationTestingClient]
):
    SERVICE_NAME = "apptest"
    _SERVICE_PROP = "apptest"
