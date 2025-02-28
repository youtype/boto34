"""
Wrapper for aioboto3 DynamoDB service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_dynamodb/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_dynamodb.client import DynamoDBClient
from types_aiobotocore_dynamodb.service_resource import DynamoDBServiceResource

from boto34.aioboto3.service_factory import ServiceResourceFactory


class DynamoDBService(ServiceResourceFactory[DynamoDBClient, DynamoDBServiceResource]):
    """
    DynamoDB service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_dynamodb/)
    """
