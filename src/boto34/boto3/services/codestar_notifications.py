"""
Wrapper for boto3 CodeStarNotifications service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_codestar_notifications/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_codestar_notifications.client import CodeStarNotificationsClient

from boto34.boto3.service_factory import ServiceFactory


class CodeStarNotificationsService(ServiceFactory[CodeStarNotificationsClient]):
    """
    CodeStarNotifications service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_codestar_notifications/)
    """
