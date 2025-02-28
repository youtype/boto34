"""
Wrapper for aioboto3 CostExplorer service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_ce/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_ce.client import CostExplorerClient

from boto34.aioboto3.service_factory import ServiceFactory


class CostExplorerService(ServiceFactory[CostExplorerClient]):
    """
    CostExplorer service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_ce/)
    """
