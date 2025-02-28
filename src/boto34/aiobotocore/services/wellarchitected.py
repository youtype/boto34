"""
Wrapper for aiobotocore WellArchitected service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_wellarchitected/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_wellarchitected.client import WellArchitectedClient

from boto34.aiobotocore.service_factory import ServiceFactory


class WellArchitectedService(ServiceFactory[WellArchitectedClient]):
    """
    WellArchitected service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_wellarchitected/)
    """
