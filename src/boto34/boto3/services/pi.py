"""
Wrapper for boto3 PI service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_pi/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_pi.client import PIClient

from boto34.boto3.service_factory import ServiceFactory


class PIService(ServiceFactory[PIClient]):
    """
    PI service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_pi/)
    """
