"""
Wrapper for boto3 Pinpoint service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_pinpoint/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_pinpoint.client import PinpointClient

from boto34.boto3.service_factory import ServiceFactory


class PinpointService(ServiceFactory[PinpointClient]):
    """
    Pinpoint service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_pinpoint/)
    """
