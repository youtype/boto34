"""
Wrapper for aioboto3 WAFRegional service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_waf_regional/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_waf_regional.client import WAFRegionalClient

from boto34.aioboto3.service_factory import ServiceFactory


class WAFRegionalService(ServiceFactory[WAFRegionalClient]):
    """
    WAFRegional service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_waf_regional/)
    """
