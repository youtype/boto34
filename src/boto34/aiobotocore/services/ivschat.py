"""
Wrapper for aiobotocore Ivschat service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivschat/)

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
    # Returns type annotated aiobotocore Ivschat client
    async with session.ivschat.create_client() as ivschat_client:
        ivschat_client: types_aiobotocore_ivschat.client.IvschatClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_ivschat.client import IvschatClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_ivschat.client import IvschatClient
except ImportError:
    IvschatClient = object  # type: ignore[misc,assignment]


class IvschatService(
    ServiceFactory[IvschatClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "ivschat"
    _SERVICE_PROP = "ivschat"
