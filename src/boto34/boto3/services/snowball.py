"""
Wrapper for boto3 Snowball service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_snowball/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_snowball.client import SnowballClient

from boto34.boto3.service_factory import ServiceFactory


class SnowballService(ServiceFactory[SnowballClient]):
    """
    Snowball service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_snowball/)
    """
