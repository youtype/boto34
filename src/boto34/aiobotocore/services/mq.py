"""
Wrapper for aiobotocore MQ service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mq/)

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
    # Returns type annotated aiobotocore MQ client
    async with session.mq.create_client() as mq_client:
        mq_client: types_aiobotocore_mq.client.MQClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_mq.client import MQClient
except ImportError:
    MQClient = object  # type: ignore[misc,assignment]


class MQService(
    ServiceFactory[MQClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "mq"
    _SERVICE_PROP = "mq"
