"""
Wrapper for aiobotocore SES service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ses/)

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
    # Returns type annotated aiobotocore SES client
    async with session.ses.create_client() as ses_client:
        ses_client: types_aiobotocore_ses.client.SESClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_ses.client import SESClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_ses.client import SESClient
except ImportError:
    SESClient = object  # type: ignore[misc,assignment]


class SESService(
    ServiceFactory[SESClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "ses"
    _SERVICE_PROP = "ses"
