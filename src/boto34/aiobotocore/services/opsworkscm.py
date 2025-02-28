"""
Wrapper for aiobotocore OpsWorksCM service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opsworkscm/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_opsworkscm.client import OpsWorksCMClient

from boto34.aiobotocore.service_factory import ServiceFactory


class OpsWorksCMService(ServiceFactory[OpsWorksCMClient]):
    """
    OpsWorksCM service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opsworkscm/)
    """
