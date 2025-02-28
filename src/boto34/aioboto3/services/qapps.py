"""
Wrapper for aioboto3 QApps service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_qapps/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_qapps.client import QAppsClient

from boto34.aioboto3.service_factory import ServiceFactory


class QAppsService(ServiceFactory[QAppsClient]):
    """
    QApps service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_qapps/)
    """
