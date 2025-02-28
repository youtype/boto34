"""
Wrapper for boto3 QApps service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_qapps/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_qapps.client import QAppsClient

from boto34.boto3.service_factory import ServiceFactory


class QAppsService(ServiceFactory[QAppsClient]):
    """
    QApps service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_qapps/)
    """
