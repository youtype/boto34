"""
Wrapper for aiobotocore KinesisAnalyticsV2 service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisanalyticsv2/)

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
    # Returns type annotated aiobotocore KinesisAnalyticsV2 client
    async with session.kinesisanalyticsv2.create_client() as kinesisanalyticsv2_client:
        kinesisanalyticsv2_client: types_aiobotocore_kinesisanalyticsv2.client.KinesisAnalyticsV2Client
    ```
"""

from __future__ import annotations

from types_aiobotocore_kinesisanalyticsv2.client import KinesisAnalyticsV2Client

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_kinesisanalyticsv2.client import KinesisAnalyticsV2Client
except ImportError:
    KinesisAnalyticsV2Client = object  # type: ignore[misc,assignment]


class KinesisAnalyticsV2Service(
    ServiceFactory[KinesisAnalyticsV2Client]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "kinesisanalyticsv2"
    _SERVICE_PROP = "kinesisanalyticsv2"
