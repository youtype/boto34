"""
Wrapper for aioboto3 WAFRegional service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_waf_regional/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aioboto3 import Session

    # Wrapper for aioboto3.Session constructor
    # Returns boto34.Session inherited from aioboto3.Session
    session = Session()
    session: boto34.aioboto3.session.Session

    # Type annotated aioboto3.Client
    # Uses the same arguments as aioboto3.client method
    # Returns type annotated aioboto3 WAFRegional client
    waf_regional_client = session.waf_regional.client()
    waf_regional_client: types_aiobotocore_waf_regional.client.WAFRegionalClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_waf_regional.client import WAFRegionalClient
except ImportError:
    WAFRegionalClient = object  # type: ignore[misc,assignment]


class WAFRegionalService(
    ServiceFactory[WAFRegionalClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "waf-regional"
    _SERVICE_PROP = "waf_regional"
