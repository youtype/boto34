"""
Wrapper for aioboto3 MQ service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_mq/)

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
    # Returns type annotated aioboto3 MQ client
    mq_client = session.mq.client()
    mq_client: types_aiobotocore_mq.client.MQClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_mq.client import MQClient

from boto34.aioboto3.service_factory import ServiceFactory


class MQService(ServiceFactory[MQClient]):
    SERVICE_NAME = "mq"
    _SERVICE_PROP = "mq"
