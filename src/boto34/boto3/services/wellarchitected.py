"""
Wrapper for boto3 WellArchitected service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_wellarchitected/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_wellarchitected.client import WellArchitectedClient

from boto34.boto3.service_factory import ServiceFactory


class WellArchitectedService(ServiceFactory[WellArchitectedClient]):
    """
    WellArchitected service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_wellarchitected/)
    """
