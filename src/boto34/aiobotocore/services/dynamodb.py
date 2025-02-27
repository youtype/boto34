"""
Wrapper for aiobotocore DynamoDB service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dynamodb/)

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
    # Returns type annotated aiobotocore DynamoDB client
    async with session.dynamodb.create_client() as dynamodb_client:
        dynamodb_client: types_aiobotocore_dynamodb.client.DynamoDBClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_dynamodb.client import DynamoDBClient

from boto34.aiobotocore.service_factory import ServiceFactory


class DynamoDBService(ServiceFactory[DynamoDBClient]):
    SERVICE_NAME = "dynamodb"
    _SERVICE_PROP = "dynamodb"
