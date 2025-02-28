"""
Wrapper for boto3 B2BI service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_b2bi/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_b2bi.client import B2BIClient

from boto34.boto3.service_factory import ServiceFactory


class B2BIService(ServiceFactory[B2BIClient]):
    """
    B2BI service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_b2bi/)
    """
