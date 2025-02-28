"""
Wrapper for boto3 Drs service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_drs/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_drs.client import DrsClient

from boto34.boto3.service_factory import ServiceFactory


class DrsService(ServiceFactory[DrsClient]):
    """
    Drs service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_drs/)
    """
