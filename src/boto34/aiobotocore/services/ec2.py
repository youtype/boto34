"""
Wrapper for aiobotocore EC2 service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_ec2.client import EC2Client

from boto34.aiobotocore.service_factory import ServiceFactory


class EC2Service(ServiceFactory[EC2Client]):
    """
    EC2 service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/)
    """
