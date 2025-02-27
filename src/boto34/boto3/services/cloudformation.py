"""
Wrapper for boto3 CloudFormation service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cloudformation/)

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
    # Returns type annotated boto3 CloudFormation client
    cloudformation_client = session.cloudformation.client()
    cloudformation_client: types_boto3_cloudformation.client.CloudFormationClient

    # Type annotated boto3.Resource
    # Uses the same arguments as boto3.resource method
    # returns type annotated boto3 CloudFormation resource
    cloudformation_resource = session.cloudformation.resource()
    cloudformation_resource: types_boto3_cloudformation.service_resource.CloudFormationServiceResource
    ```
"""

from __future__ import annotations

from types_boto3_cloudformation.client import CloudFormationClient
from types_boto3_cloudformation.service_resource import CloudFormationServiceResource

from boto34.boto3.service_factory import ServiceResourceFactory


class CloudFormationService(
    ServiceResourceFactory[CloudFormationClient, CloudFormationServiceResource]
):
    SERVICE_NAME = "cloudformation"
    _SERVICE_PROP = "cloudformation"
