"""
Wrapper for aioboto3 CloudFormation service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_cloudformation/)

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
    # Returns type annotated aioboto3 CloudFormation client
    cloudformation_client = session.cloudformation.client()
    cloudformation_client: types_aiobotocore_cloudformation.client.CloudFormationClient

    # Type annotated aioboto3.Resource
    # Uses the same arguments as aioboto3.resource method
    # returns type annotated aioboto3 CloudFormation resource
    cloudformation_resource = session.cloudformation.resource()
    cloudformation_resource: (
        types_aiobotocore_cloudformation.service_resource.CloudFormationServiceResource
    )
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceResourceFactory

try:
    from types_aiobotocore_cloudformation.client import CloudFormationClient
    from types_aiobotocore_cloudformation.service_resource import CloudFormationServiceResource
except ImportError:
    CloudFormationClient = object  # type: ignore[misc,assignment]
    CloudFormationServiceResource = object  # type: ignore[misc,assignment]


class CloudFormationService(
    ServiceResourceFactory[CloudFormationClient, CloudFormationServiceResource]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "cloudformation"
    _SERVICE_PROP = "cloudformation"
