"""
Wrapper for boto3 RePostPrivate service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_repostspace/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_repostspace.client import RePostPrivateClient

from boto34.boto3.service_factory import ServiceFactory


class RePostPrivateService(ServiceFactory[RePostPrivateClient]):
    """
    RePostPrivate service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_repostspace/)
    """
