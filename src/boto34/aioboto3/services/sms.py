"""
Wrapper for aioboto3 SMS service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_sms/)

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
    # Returns type annotated aioboto3 SMS client
    sms_client = session.sms.client()
    sms_client: types_aiobotocore_sms.client.SMSClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_sms.client import SMSClient
except ImportError:
    SMSClient = object  # type: ignore[misc,assignment]


class SMSService(
    ServiceFactory[SMSClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "sms"
    _SERVICE_PROP = "sms"
