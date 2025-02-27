"""
Wrapper for aiobotocore WAF service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_waf/)

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
    # Returns type annotated aiobotocore WAF client
    async with session.waf.create_client() as waf_client:
        waf_client: types_aiobotocore_waf.client.WAFClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_waf.client import WAFClient
except ImportError:
    WAFClient = object  # type: ignore[misc,assignment]


class WAFService(
    ServiceFactory[WAFClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "waf"
    _SERVICE_PROP = "waf"
