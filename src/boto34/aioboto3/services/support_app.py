"""
Wrapper for aioboto3 SupportApp service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_support_app/)

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
    # Returns type annotated aioboto3 SupportApp client
    support_app_client = session.support_app.client()
    support_app_client: types_aiobotocore_support_app.client.SupportAppClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_support_app.client import SupportAppClient
except ImportError:
    SupportAppClient = object  # type: ignore[misc,assignment]


class SupportAppService(
    ServiceFactory[SupportAppClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "support-app"
    _SERVICE_PROP = "support_app"
