"""
Wrapper for boto3 Lightsail service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_lightsail/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_lightsail.client import LightsailClient

from boto34.boto3.service_factory import ServiceFactory


class LightsailService(ServiceFactory[LightsailClient]):
    """
    Lightsail service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_lightsail/)
    """
