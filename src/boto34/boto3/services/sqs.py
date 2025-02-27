"""
Wrapper for boto3 SQS service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_sqs/)

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
    # Returns type annotated boto3 SQS client
    sqs_client = session.sqs.client()
    sqs_client: types_boto3_sqs.client.SQSClient

    # Type annotated boto3.Resource
    # Uses the same arguments as boto3.resource method
    # returns type annotated boto3 SQS resource
    sqs_resource = session.sqs.resource()
    sqs_resource: types_boto3_sqs.service_resource.SQSServiceResource
    ```
"""

from __future__ import annotations

from types_boto3_sqs.client import SQSClient
from types_boto3_sqs.service_resource import SQSServiceResource

from boto34.boto3.service_factory import ServiceResourceFactory


class SQSService(ServiceResourceFactory[SQSClient, SQSServiceResource]):
    SERVICE_NAME = "sqs"
    _SERVICE_PROP = "sqs"
