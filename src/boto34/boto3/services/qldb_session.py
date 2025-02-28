"""
Wrapper for boto3 QLDBSession service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_qldb_session/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_qldb_session.client import QLDBSessionClient

from boto34.boto3.service_factory import ServiceFactory


class QLDBSessionService(ServiceFactory[QLDBSessionClient]):
    """
    QLDBSession service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_qldb_session/)
    """
