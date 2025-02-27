"""
Wrapper for aioboto3 DynamoDB service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_dynamodb/)

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
    # Returns type annotated aioboto3 DynamoDB client
    dynamodb_client = session.dynamodb.client()
    dynamodb_client: types_aiobotocore_dynamodb.client.DynamoDBClient

    # Type annotated aioboto3.Resource
    # Uses the same arguments as aioboto3.resource method
    # returns type annotated aioboto3 DynamoDB resource
    dynamodb_resource = session.dynamodb.resource()
    dynamodb_resource: types_aiobotocore_dynamodb.service_resource.DynamoDBServiceResource
    ```
"""

from __future__ import annotations

from types_aiobotocore_dynamodb.client import DynamoDBClient
from types_aiobotocore_dynamodb.service_resource import DynamoDBServiceResource

from boto34.aioboto3.service_factory import ServiceResourceFactory


class DynamoDBService(ServiceResourceFactory[DynamoDBClient, DynamoDBServiceResource]):
    SERVICE_NAME = "dynamodb"
    _SERVICE_PROP = "dynamodb"
