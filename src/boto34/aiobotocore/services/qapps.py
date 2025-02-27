"""
Wrapper for aiobotocore QApps service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qapps/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore QApps client
    async with session.qapps.create_client() as qapps_client:
        qapps_client: types_aiobotocore_qapps.client.QAppsClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_qapps.client import QAppsClient
except ImportError:
    QAppsClient = object  # type: ignore[misc,assignment]


class QAppsService(
    ServiceFactory[QAppsClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "qapps"
    _SERVICE_PROP = "qapps"
