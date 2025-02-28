"""
Wrapper for boto3 Ivsrealtime service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_ivs_realtime/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_ivs_realtime.client import IvsrealtimeClient

from boto34.boto3.service_factory import ServiceFactory


class IvsrealtimeService(ServiceFactory[IvsrealtimeClient]):
    """
    Ivsrealtime service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_ivs_realtime/)
    """
