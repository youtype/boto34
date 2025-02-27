"""
Wrapper for aiobotocore SupportApp service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_support_app/)

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
    # Returns type annotated aiobotocore SupportApp client
    async with session.support_app.create_client() as support_app_client:
        support_app_client: types_aiobotocore_support_app.client.SupportAppClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_support_app.client import SupportAppClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_support_app.client import SupportAppClient
except ImportError:
    SupportAppClient = object  # type: ignore[misc,assignment]


class SupportAppService(
    ServiceFactory[SupportAppClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "support-app"
    _SERVICE_PROP = "support_app"
