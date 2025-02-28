"""
Wrapper for boto3 QuickSight service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_quicksight/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_quicksight.client import QuickSightClient

from boto34.boto3.service_factory import ServiceFactory


class QuickSightService(ServiceFactory[QuickSightClient]):
    """
    QuickSight service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_quicksight/)
    """
