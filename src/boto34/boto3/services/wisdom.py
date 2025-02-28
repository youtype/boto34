"""
Wrapper for boto3 ConnectWisdomService service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_wisdom/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_wisdom.client import ConnectWisdomServiceClient

from boto34.boto3.service_factory import ServiceFactory


class ConnectWisdomServiceService(ServiceFactory[ConnectWisdomServiceClient]):
    """
    ConnectWisdomService service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_wisdom/)
    """
