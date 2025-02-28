"""
Wrapper for aioboto3 CleanRoomsService service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_cleanrooms/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_cleanrooms.client import CleanRoomsServiceClient

from boto34.aioboto3.service_factory import ServiceFactory


class CleanRoomsServiceService(ServiceFactory[CleanRoomsServiceClient]):
    """
    CleanRoomsService service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_cleanrooms/)
    """
