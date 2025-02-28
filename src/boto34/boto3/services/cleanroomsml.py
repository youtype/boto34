"""
Wrapper for boto3 CleanRoomsML service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cleanroomsml/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_cleanroomsml.client import CleanRoomsMLClient

from boto34.boto3.service_factory import ServiceFactory


class CleanRoomsMLService(ServiceFactory[CleanRoomsMLClient]):
    """
    CleanRoomsML service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cleanroomsml/)
    """
