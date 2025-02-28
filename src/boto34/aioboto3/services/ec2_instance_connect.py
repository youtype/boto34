"""
Wrapper for aioboto3 EC2InstanceConnect service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_ec2_instance_connect/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_ec2_instance_connect.client import EC2InstanceConnectClient

from boto34.aioboto3.service_factory import ServiceFactory


class EC2InstanceConnectService(ServiceFactory[EC2InstanceConnectClient]):
    """
    EC2InstanceConnect service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_ec2_instance_connect/)
    """
