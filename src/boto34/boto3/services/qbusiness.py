"""
Wrapper for boto3 QBusiness service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_qbusiness/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_qbusiness.client import QBusinessClient

from boto34.boto3.service_factory import ServiceFactory


class QBusinessService(ServiceFactory[QBusinessClient]):
    """
    QBusiness service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_qbusiness/)
    """
