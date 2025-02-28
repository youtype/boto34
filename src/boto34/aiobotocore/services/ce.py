"""
Wrapper for aiobotocore CostExplorer service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ce/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_ce.client import CostExplorerClient

from boto34.aiobotocore.service_factory import ServiceFactory


class CostExplorerService(ServiceFactory[CostExplorerClient]):
    """
    CostExplorer service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ce/)
    """
