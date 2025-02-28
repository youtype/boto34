"""
Wrapper for boto3 MWAA service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_mwaa/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_mwaa.client import MWAAClient

from boto34.boto3.service_factory import ServiceFactory


class MWAAService(ServiceFactory[MWAAClient]):
    """
    MWAA service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_mwaa/)
    """
