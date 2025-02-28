"""
Wrapper for boto3 Shield service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_shield/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_shield.client import ShieldClient

from boto34.boto3.service_factory import ServiceFactory


class ShieldService(ServiceFactory[ShieldClient]):
    """
    Shield service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_shield/)
    """
