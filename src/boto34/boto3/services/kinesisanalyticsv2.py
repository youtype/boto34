"""
Wrapper for boto3 KinesisAnalyticsV2 service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_kinesisanalyticsv2/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.boto3 import Session

    # Wrapper for boto3.Session constructor
    # Returns boto34.Session inherited from boto3.Session
    session = Session()
    session: boto34.boto3.session.Session

    # Type annotated boto3.Client
    # Uses the same arguments as boto3.client method
    # Returns type annotated boto3 KinesisAnalyticsV2 client
    kinesisanalyticsv2_client = session.kinesisanalyticsv2.client()
    kinesisanalyticsv2_client: types_boto3_kinesisanalyticsv2.client.KinesisAnalyticsV2Client
    ```
"""

from __future__ import annotations

from types_boto3_kinesisanalyticsv2.client import KinesisAnalyticsV2Client

from boto34.boto3.service_factory import ServiceFactory


class KinesisAnalyticsV2Service(ServiceFactory[KinesisAnalyticsV2Client]):
    SERVICE_NAME = "kinesisanalyticsv2"
    _SERVICE_PROP = "kinesisanalyticsv2"
