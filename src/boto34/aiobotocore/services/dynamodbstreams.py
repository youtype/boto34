"""
Wrapper for aiobotocore DynamoDBStreams service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dynamodbstreams/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_dynamodbstreams.client import DynamoDBStreamsClient

from boto34.aiobotocore.service_factory import ServiceFactory


class DynamoDBStreamsService(ServiceFactory[DynamoDBStreamsClient]):
    """
    DynamoDBStreams service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dynamodbstreams/)
    """
