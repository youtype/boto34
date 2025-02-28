"""
Wrapper for boto3 DynamoDB service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_dynamodb/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_dynamodb.client import DynamoDBClient
from types_boto3_dynamodb.service_resource import DynamoDBServiceResource

from boto34.boto3.service_factory import ServiceResourceFactory


class DynamoDBService(ServiceResourceFactory[DynamoDBClient, DynamoDBServiceResource]):
    """
    DynamoDB service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_dynamodb/)
    """
