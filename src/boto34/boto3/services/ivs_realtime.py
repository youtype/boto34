"""
Wrapper for boto3 Ivsrealtime service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_ivs_realtime/)

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
    # Returns type annotated boto3 Ivsrealtime client
    ivs_realtime_client = session.ivs_realtime.client()
    ivs_realtime_client: types_boto3_ivs_realtime.client.IvsrealtimeClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_ivs_realtime.client import IvsrealtimeClient
except ImportError:
    IvsrealtimeClient = object  # type: ignore[misc,assignment]


class IvsrealtimeService(
    ServiceFactory[IvsrealtimeClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "ivs-realtime"
    _SERVICE_PROP = "ivs_realtime"
