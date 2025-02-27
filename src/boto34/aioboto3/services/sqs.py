"""
Wrapper for aioboto3 SQS service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_sqs/)

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
    # Returns type annotated aioboto3 SQS client
    sqs_client = session.sqs.client()
    sqs_client: types_aiobotocore_sqs.client.SQSClient

    # Type annotated aioboto3.Resource
    # Uses the same arguments as aioboto3.resource method
    # returns type annotated aioboto3 SQS resource
    sqs_resource = session.sqs.resource()
    sqs_resource: types_aiobotocore_sqs.service_resource.SQSServiceResource
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceResourceFactory

try:
    from types_aiobotocore_sqs.client import SQSClient
    from types_aiobotocore_sqs.service_resource import SQSServiceResource
except ImportError:
    SQSClient = object  # type: ignore[misc,assignment]
    SQSServiceResource = object  # type: ignore[misc,assignment]


class SQSService(
    ServiceResourceFactory[SQSClient, SQSServiceResource]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "sqs"
    _SERVICE_PROP = "sqs"
