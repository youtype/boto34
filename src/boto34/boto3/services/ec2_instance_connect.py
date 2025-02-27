"""
Wrapper for boto3 EC2InstanceConnect service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_ec2_instance_connect/)

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
    # Returns type annotated boto3 EC2InstanceConnect client
    ec2_instance_connect_client = session.ec2_instance_connect.client()
    ec2_instance_connect_client: types_boto3_ec2_instance_connect.client.EC2InstanceConnectClient
    ```
"""

from __future__ import annotations

from types_boto3_ec2_instance_connect.client import EC2InstanceConnectClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_ec2_instance_connect.client import EC2InstanceConnectClient
except ImportError:
    EC2InstanceConnectClient = object  # type: ignore[misc,assignment]


class EC2InstanceConnectService(
    ServiceFactory[EC2InstanceConnectClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "ec2-instance-connect"
    _SERVICE_PROP = "ec2_instance_connect"
