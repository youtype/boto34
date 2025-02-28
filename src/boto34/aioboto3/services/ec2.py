"""
Wrapper for aioboto3 EC2 service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_ec2/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_ec2.client import EC2Client
from types_aiobotocore_ec2.service_resource import EC2ServiceResource

from boto34.aioboto3.service_factory import ServiceResourceFactory


class EC2Service(ServiceResourceFactory[EC2Client, EC2ServiceResource]):
    """
    EC2 service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_ec2/)
    """
