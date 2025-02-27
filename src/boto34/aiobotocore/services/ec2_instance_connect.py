"""
Wrapper for aiobotocore EC2InstanceConnect service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2_instance_connect/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore EC2InstanceConnect client
    async with session.ec2_instance_connect.create_client() as ec2_instance_connect_client:
        ec2_instance_connect_client: (
            types_aiobotocore_ec2_instance_connect.client.EC2InstanceConnectClient
        )
    ```
"""

from __future__ import annotations

from types_aiobotocore_ec2_instance_connect.client import EC2InstanceConnectClient

from boto34.aiobotocore.service_factory import ServiceFactory


class EC2InstanceConnectService(ServiceFactory[EC2InstanceConnectClient]):
    SERVICE_NAME = "ec2-instance-connect"
    _SERVICE_PROP = "ec2_instance_connect"
