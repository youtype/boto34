"""
Wrapper for aioboto3 WorkMail service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_workmail/)

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
    # Returns type annotated aioboto3 WorkMail client
    workmail_client = session.workmail.client()
    workmail_client: types_aiobotocore_workmail.client.WorkMailClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_workmail.client import WorkMailClient

from boto34.aioboto3.service_factory import ServiceFactory


class WorkMailService(ServiceFactory[WorkMailClient]):
    SERVICE_NAME = "workmail"
    _SERVICE_PROP = "workmail"
