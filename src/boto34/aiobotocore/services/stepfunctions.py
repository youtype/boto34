"""
Wrapper for aiobotocore SFN service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_stepfunctions/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_stepfunctions.client import SFNClient

from boto34.aiobotocore.service_factory import ServiceFactory


class SFNService(ServiceFactory[SFNClient]):
    """
    SFN service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_stepfunctions/)
    """
