"""
Wrapper for boto3 DeadlineCloud service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_deadline/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_deadline.client import DeadlineCloudClient

from boto34.boto3.service_factory import ServiceFactory


class DeadlineCloudService(ServiceFactory[DeadlineCloudClient]):
    """
    DeadlineCloud service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_deadline/)
    """
