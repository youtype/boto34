"""
Wrapper for aiobotocore QuickSight service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_quicksight/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_quicksight.client import QuickSightClient

from boto34.aiobotocore.service_factory import ServiceFactory


class QuickSightService(ServiceFactory[QuickSightClient]):
    """
    QuickSight service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_quicksight/)
    """
