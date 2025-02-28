"""
Wrapper for boto3 CleanRoomsService service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cleanrooms/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_cleanrooms.client import CleanRoomsServiceClient

from boto34.boto3.service_factory import ServiceFactory


class CleanRoomsServiceService(ServiceFactory[CleanRoomsServiceClient]):
    """
    CleanRoomsService service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cleanrooms/)
    """
