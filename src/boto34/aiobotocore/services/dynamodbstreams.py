"""
Wrapper for aiobotocore DynamoDBStreams service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dynamodbstreams/)

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
    # Returns type annotated aiobotocore DynamoDBStreams client
    async with session.dynamodbstreams.create_client() as dynamodbstreams_client:
        dynamodbstreams_client: types_aiobotocore_dynamodbstreams.client.DynamoDBStreamsClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_dynamodbstreams.client import DynamoDBStreamsClient

from boto34.aiobotocore.service_factory import ServiceFactory


class DynamoDBStreamsService(ServiceFactory[DynamoDBStreamsClient]):
    SERVICE_NAME = "dynamodbstreams"
    _SERVICE_PROP = "dynamodbstreams"
