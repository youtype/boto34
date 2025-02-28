"""
Wrapper for aiobotocore SimSpaceWeaver service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_simspaceweaver/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_simspaceweaver.client import SimSpaceWeaverClient

from boto34.aiobotocore.service_factory import ServiceFactory


class SimSpaceWeaverService(ServiceFactory[SimSpaceWeaverClient]):
    """
    SimSpaceWeaver service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_simspaceweaver/)
    """
