"""
Wrapper for boto3 DynamoDB service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_dynamodb/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.boto3 import Session

    # Wrapper for boto3.Session constructor
    # Returns boto34.Session inherited from boto3.Session
    session = Session()
    session: boto34.boto3.session.Session

    # Type annotated boto3.Client
    # Uses the same arguments as boto3.client method
    # Returns type annotated boto3 DynamoDB client
    dynamodb_client = session.dynamodb.client()
    dynamodb_client: types_boto3_dynamodb.client.DynamoDBClient

    # Type annotated boto3.Resource
    # Uses the same arguments as boto3.resource method
    # returns type annotated boto3 DynamoDB resource
    dynamodb_resource = session.dynamodb.resource()
    dynamodb_resource: types_boto3_dynamodb.service_resource.DynamoDBServiceResource
    ```
"""

from __future__ import annotations

from types_boto3_dynamodb.client import DynamoDBClient
from types_boto3_dynamodb.service_resource import DynamoDBServiceResource

from boto34.boto3.service_factory import ServiceResourceFactory


class DynamoDBService(ServiceResourceFactory[DynamoDBClient, DynamoDBServiceResource]):
    SERVICE_NAME = "dynamodb"
    _SERVICE_PROP = "dynamodb"
