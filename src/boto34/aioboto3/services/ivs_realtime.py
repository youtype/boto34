"""
Wrapper for aioboto3 Ivsrealtime service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_ivs_realtime/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_ivs_realtime.client import IvsrealtimeClient

from boto34.aioboto3.service_factory import ServiceFactory


class IvsrealtimeService(ServiceFactory[IvsrealtimeClient]):
    """
    Ivsrealtime service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_ivs_realtime/)
    """
