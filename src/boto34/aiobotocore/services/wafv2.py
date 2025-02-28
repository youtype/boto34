"""
Wrapper for aiobotocore WAFV2 service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_wafv2/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_wafv2.client import WAFV2Client

from boto34.aiobotocore.service_factory import ServiceFactory


class WAFV2Service(ServiceFactory[WAFV2Client]):
    """
    WAFV2 service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_wafv2/)
    """
