"""
Wrapper for aiobotocore EC2 service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/)

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
    # Returns type annotated aiobotocore EC2 client
    async with session.ec2.create_client() as ec2_client:
        ec2_client: types_aiobotocore_ec2.client.EC2Client
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_ec2.client import EC2Client
except ImportError:
    EC2Client = object  # type: ignore[misc,assignment]


class EC2Service(
    ServiceFactory[EC2Client]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "ec2"
    _SERVICE_PROP = "ec2"
