"""
Wrapper for aioboto3 SNS service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_sns/)

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
    # Returns type annotated aioboto3 SNS client
    sns_client = session.sns.client()
    sns_client: types_aiobotocore_sns.client.SNSClient

    # Type annotated aioboto3.Resource
    # Uses the same arguments as aioboto3.resource method
    # returns type annotated aioboto3 SNS resource
    sns_resource = session.sns.resource()
    sns_resource: types_aiobotocore_sns.service_resource.SNSServiceResource
    ```
"""

from __future__ import annotations

from types_aiobotocore_sns.client import SNSClient
from types_aiobotocore_sns.service_resource import SNSServiceResource

from boto34.aioboto3.service_factory import ServiceResourceFactory


class SNSService(ServiceResourceFactory[SNSClient, SNSServiceResource]):
    SERVICE_NAME = "sns"
    _SERVICE_PROP = "sns"
