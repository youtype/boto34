"""
Wrapper for boto3 SNS service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_sns/)

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
    # Returns type annotated boto3 SNS client
    sns_client = session.sns.client()
    sns_client: types_boto3_sns.client.SNSClient

    # Type annotated boto3.Resource
    # Uses the same arguments as boto3.resource method
    # returns type annotated boto3 SNS resource
    sns_resource = session.sns.resource()
    sns_resource: types_boto3_sns.service_resource.SNSServiceResource
    ```
"""

from __future__ import annotations

from types_boto3_sns.client import SNSClient
from types_boto3_sns.service_resource import SNSServiceResource

from boto34.boto3.service_factory import ServiceResourceFactory


class SNSService(ServiceResourceFactory[SNSClient, SNSServiceResource]):
    SERVICE_NAME = "sns"
    _SERVICE_PROP = "sns"
