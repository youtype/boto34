"""
Wrapper for boto3 WorkMail service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_workmail/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_workmail.client import WorkMailClient

from boto34.boto3.service_factory import ServiceFactory


class WorkMailService(ServiceFactory[WorkMailClient]):
    """
    WorkMail service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_workmail/)
    """
