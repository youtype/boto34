"""
Wrapper for aiobotocore DynamoDB service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dynamodb/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_dynamodb.client import DynamoDBClient

from boto34.aiobotocore.service_factory import ServiceFactory


class DynamoDBService(ServiceFactory[DynamoDBClient]):
    """
    DynamoDB service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dynamodb/)
    """
