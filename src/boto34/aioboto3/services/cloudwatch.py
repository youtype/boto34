"""
Wrapper for aioboto3 CloudWatch service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_cloudwatch/)

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
    # Returns type annotated aioboto3 CloudWatch client
    cloudwatch_client = session.cloudwatch.client()
    cloudwatch_client: types_aiobotocore_cloudwatch.client.CloudWatchClient

    # Type annotated aioboto3.Resource
    # Uses the same arguments as aioboto3.resource method
    # returns type annotated aioboto3 CloudWatch resource
    cloudwatch_resource = session.cloudwatch.resource()
    cloudwatch_resource: types_aiobotocore_cloudwatch.service_resource.CloudWatchServiceResource
    ```
"""

from __future__ import annotations

from types_aiobotocore_cloudwatch.client import CloudWatchClient
from types_aiobotocore_cloudwatch.service_resource import CloudWatchServiceResource

from boto34.aioboto3.service_factory import ServiceResourceFactory


class CloudWatchService(ServiceResourceFactory[CloudWatchClient, CloudWatchServiceResource]):
    SERVICE_NAME = "cloudwatch"
    _SERVICE_PROP = "cloudwatch"
