"""
Wrapper for boto3 Synthetics service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_synthetics/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_synthetics.client import SyntheticsClient

from boto34.boto3.service_factory import ServiceFactory


class SyntheticsService(ServiceFactory[SyntheticsClient]):
    """
    Synthetics service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_synthetics/)
    """
