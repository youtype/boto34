"""
Wrapper for aiobotocore WAFRegional service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_waf_regional/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore WAFRegional client
    async with session.waf_regional.create_client() as waf_regional_client:
        waf_regional_client: types_aiobotocore_waf_regional.client.WAFRegionalClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_waf_regional.client import WAFRegionalClient
except ImportError:
    WAFRegionalClient = object  # type: ignore[misc,assignment]


class WAFRegionalService(
    ServiceFactory[WAFRegionalClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "waf-regional"
    _SERVICE_PROP = "waf_regional"
