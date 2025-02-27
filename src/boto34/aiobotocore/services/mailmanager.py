"""
Wrapper for aiobotocore MailManager service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mailmanager/)

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
    # Returns type annotated aiobotocore MailManager client
    async with session.mailmanager.create_client() as mailmanager_client:
        mailmanager_client: types_aiobotocore_mailmanager.client.MailManagerClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_mailmanager.client import MailManagerClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_mailmanager.client import MailManagerClient
except ImportError:
    MailManagerClient = object  # type: ignore[misc,assignment]


class MailManagerService(
    ServiceFactory[MailManagerClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "mailmanager"
    _SERVICE_PROP = "mailmanager"
