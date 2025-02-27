"""
Wrapper for aioboto3 MailManager service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_mailmanager/)

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
    # Returns type annotated aioboto3 MailManager client
    mailmanager_client = session.mailmanager.client()
    mailmanager_client: types_aiobotocore_mailmanager.client.MailManagerClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_mailmanager.client import MailManagerClient

from boto34.aioboto3.service_factory import ServiceFactory


class MailManagerService(ServiceFactory[MailManagerClient]):
    SERVICE_NAME = "mailmanager"
    _SERVICE_PROP = "mailmanager"
