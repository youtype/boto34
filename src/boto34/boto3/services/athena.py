"""
Wrapper for boto3 Athena service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_athena/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_athena.client import AthenaClient

from boto34.boto3.service_factory import ServiceFactory


class AthenaService(ServiceFactory[AthenaClient]):
    """
    Athena service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_athena/)
    """
