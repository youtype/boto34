"""
Wrapper for boto3 EC2 service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_ec2/)

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
    # Returns type annotated boto3 EC2 client
    ec2_client = session.ec2.client()
    ec2_client: types_boto3_ec2.client.EC2Client

    # Type annotated boto3.Resource
    # Uses the same arguments as boto3.resource method
    # returns type annotated boto3 EC2 resource
    ec2_resource = session.ec2.resource()
    ec2_resource: types_boto3_ec2.service_resource.EC2ServiceResource
    ```
"""

from __future__ import annotations

from types_boto3_ec2.client import EC2Client

from boto34.boto3.service_factory import ServiceResourceFactory

try:
    from types_boto3_ec2.client import EC2Client
    from types_boto3_ec2.service_resource import EC2ServiceResource
except ImportError:
    EC2Client = object  # type: ignore[misc,assignment]
    EC2ServiceResource = object  # type: ignore[misc,assignment]


class EC2Service(
    ServiceResourceFactory[EC2Client, EC2ServiceResource]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "ec2"
    _SERVICE_PROP = "ec2"
