"""
Wrapper for aiobotocore Ivsrealtime service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivs_realtime/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_ivs_realtime.client import IvsrealtimeClient

from boto34.aiobotocore.service_factory import ServiceFactory


class IvsrealtimeService(ServiceFactory[IvsrealtimeClient]):
    """
    Ivsrealtime service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivs_realtime/)
    """
