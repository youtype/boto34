"""
Wrapper for boto3 DynamoDBStreams service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_dynamodbstreams/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_dynamodbstreams.client import DynamoDBStreamsClient

from boto34.boto3.service_factory import ServiceFactory


class DynamoDBStreamsService(ServiceFactory[DynamoDBStreamsClient]):
    """
    DynamoDBStreams service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_dynamodbstreams/)
    """
