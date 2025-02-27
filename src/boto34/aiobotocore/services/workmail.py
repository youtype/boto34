"""
Wrapper for aiobotocore WorkMail service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workmail/)

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
    # Returns type annotated aiobotocore WorkMail client
    async with session.workmail.create_client() as workmail_client:
        workmail_client: types_aiobotocore_workmail.client.WorkMailClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_workmail.client import WorkMailClient

from boto34.aiobotocore.service_factory import ServiceFactory


class WorkMailService(ServiceFactory[WorkMailClient]):
    SERVICE_NAME = "workmail"
    _SERVICE_PROP = "workmail"
