"""
Wrapper for boto3 QConnect service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_qconnect/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_qconnect.client import QConnectClient

from boto34.boto3.service_factory import ServiceFactory


class QConnectService(ServiceFactory[QConnectClient]):
    """
    QConnect service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_qconnect/)
    """
