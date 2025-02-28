"""
Wrapper for boto3 Mgn service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_mgn/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_mgn.client import MgnClient

from boto34.boto3.service_factory import ServiceFactory


class MgnService(ServiceFactory[MgnClient]):
    """
    Mgn service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_mgn/)
    """
