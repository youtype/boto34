"""
Wrapper for boto3 CostExplorer service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_ce/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_ce.client import CostExplorerClient

from boto34.boto3.service_factory import ServiceFactory


class CostExplorerService(ServiceFactory[CostExplorerClient]):
    """
    CostExplorer service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_ce/)
    """
