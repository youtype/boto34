"""
Wrapper for boto3 CloudWatch service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cloudwatch/)

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
    # Returns type annotated boto3 CloudWatch client
    cloudwatch_client = session.cloudwatch.client()
    cloudwatch_client: types_boto3_cloudwatch.client.CloudWatchClient

    # Type annotated boto3.Resource
    # Uses the same arguments as boto3.resource method
    # returns type annotated boto3 CloudWatch resource
    cloudwatch_resource = session.cloudwatch.resource()
    cloudwatch_resource: types_boto3_cloudwatch.service_resource.CloudWatchServiceResource
    ```
"""

from __future__ import annotations

from types_boto3_cloudwatch.client import CloudWatchClient
from types_boto3_cloudwatch.service_resource import CloudWatchServiceResource

from boto34.boto3.service_factory import ServiceResourceFactory


class CloudWatchService(ServiceResourceFactory[CloudWatchClient, CloudWatchServiceResource]):
    SERVICE_NAME = "cloudwatch"
    _SERVICE_PROP = "cloudwatch"
