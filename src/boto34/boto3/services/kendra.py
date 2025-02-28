"""
Wrapper for boto3 Kendra service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_kendra/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_kendra.client import KendraClient

from boto34.boto3.service_factory import ServiceFactory


class KendraService(ServiceFactory[KendraClient]):
    """
    Kendra service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_kendra/)
    """
