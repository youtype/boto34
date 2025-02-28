"""
Wrapper for boto3 GreengrassV2 service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_greengrassv2/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_greengrassv2.client import GreengrassV2Client

from boto34.boto3.service_factory import ServiceFactory


class GreengrassV2Service(ServiceFactory[GreengrassV2Client]):
    """
    GreengrassV2 service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_greengrassv2/)
    """
