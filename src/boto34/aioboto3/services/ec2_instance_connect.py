"""
Wrapper for aioboto3 EC2InstanceConnect service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_ec2_instance_connect/)

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
    # Returns type annotated aioboto3 EC2InstanceConnect client
    ec2_instance_connect_client = session.ec2_instance_connect.client()
    ec2_instance_connect_client: types_aiobotocore_ec2_instance_connect.client.EC2InstanceConnectClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_ec2_instance_connect.client import EC2InstanceConnectClient
except ImportError:
    EC2InstanceConnectClient = object  # type: ignore[misc,assignment]


class EC2InstanceConnectService(
    ServiceFactory[EC2InstanceConnectClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "ec2-instance-connect"
    _SERVICE_PROP = "ec2_instance_connect"
