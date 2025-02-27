"""
Wrapper for aiobotocore SNS service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sns/)

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
    # Returns type annotated aiobotocore SNS client
    async with session.sns.create_client() as sns_client:
        sns_client: types_aiobotocore_sns.client.SNSClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_sns.client import SNSClient
except ImportError:
    SNSClient = object  # type: ignore[misc,assignment]


class SNSService(
    ServiceFactory[SNSClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "sns"
    _SERVICE_PROP = "sns"
