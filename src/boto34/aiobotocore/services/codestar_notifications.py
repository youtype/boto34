"""
Wrapper for aiobotocore CodeStarNotifications service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codestar_notifications/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_codestar_notifications.client import CodeStarNotificationsClient

from boto34.aiobotocore.service_factory import ServiceFactory


class CodeStarNotificationsService(ServiceFactory[CodeStarNotificationsClient]):
    """
    CodeStarNotifications service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codestar_notifications/)
    """
