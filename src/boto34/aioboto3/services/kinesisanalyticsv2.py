"""
Wrapper for aioboto3 KinesisAnalyticsV2 service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_kinesisanalyticsv2/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aioboto3 import Session

    # Wrapper for aioboto3.Session constructor
    # Returns boto34.Session inherited from aioboto3.Session
    session = Session()
    session: boto34.aioboto3.session.Session

    # Type annotated aioboto3.Client
    # Uses the same arguments as aioboto3.client method
    # Returns type annotated aioboto3 KinesisAnalyticsV2 client
    kinesisanalyticsv2_client = session.kinesisanalyticsv2.client()
    kinesisanalyticsv2_client: types_aiobotocore_kinesisanalyticsv2.client.KinesisAnalyticsV2Client
    ```
"""

from __future__ import annotations

from types_aiobotocore_kinesisanalyticsv2.client import KinesisAnalyticsV2Client

from boto34.aioboto3.service_factory import ServiceFactory


class KinesisAnalyticsV2Service(ServiceFactory[KinesisAnalyticsV2Client]):
    SERVICE_NAME = "kinesisanalyticsv2"
    _SERVICE_PROP = "kinesisanalyticsv2"
