"""
Wrapper for boto3 SESV2 service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_sesv2/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_sesv2.client import SESV2Client

from boto34.boto3.service_factory import ServiceFactory


class SESV2Service(ServiceFactory[SESV2Client]):
    """
    SESV2 service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_sesv2/)
    """
