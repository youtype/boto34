"""
Wrapper for boto3 IoTSecureTunneling service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_iotsecuretunneling/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_iotsecuretunneling.client import IoTSecureTunnelingClient

from boto34.boto3.service_factory import ServiceFactory


class IoTSecureTunnelingService(ServiceFactory[IoTSecureTunnelingClient]):
    """
    IoTSecureTunneling service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_iotsecuretunneling/)
    """
