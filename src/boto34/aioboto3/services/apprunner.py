"""
Wrapper for aioboto3 AppRunner service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_apprunner/)

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
    # Returns type annotated aioboto3 AppRunner client
    apprunner_client = session.apprunner.client()
    apprunner_client: types_aiobotocore_apprunner.client.AppRunnerClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_apprunner.client import AppRunnerClient

from boto34.aioboto3.service_factory import ServiceFactory


class AppRunnerService(ServiceFactory[AppRunnerClient]):
    SERVICE_NAME = "apprunner"
    _SERVICE_PROP = "apprunner"
