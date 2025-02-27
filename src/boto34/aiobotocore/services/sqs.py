"""
Wrapper for aiobotocore SQS service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sqs/)

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
    # Returns type annotated aiobotocore SQS client
    async with session.sqs.create_client() as sqs_client:
        sqs_client: types_aiobotocore_sqs.client.SQSClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_sqs.client import SQSClient
except ImportError:
    SQSClient = object  # type: ignore[misc,assignment]


class SQSService(
    ServiceFactory[SQSClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "sqs"
    _SERVICE_PROP = "sqs"
