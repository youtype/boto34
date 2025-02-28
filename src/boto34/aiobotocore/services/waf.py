"""
Wrapper for aiobotocore WAF service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_waf/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_waf.client import WAFClient

from boto34.aiobotocore.service_factory import ServiceFactory


class WAFService(ServiceFactory[WAFClient]):
    """
    WAF service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_waf/)
    """
