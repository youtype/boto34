"""
Wrapper for aiobotocore SMS service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sms/)

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
    # Returns type annotated aiobotocore SMS client
    async with session.sms.create_client() as sms_client:
        sms_client: types_aiobotocore_sms.client.SMSClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_sms.client import SMSClient

from boto34.aiobotocore.service_factory import ServiceFactory


class SMSService(ServiceFactory[SMSClient]):
    SERVICE_NAME = "sms"
    _SERVICE_PROP = "sms"
