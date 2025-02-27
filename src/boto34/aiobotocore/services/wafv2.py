"""
Wrapper for aiobotocore WAFV2 service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_wafv2/)

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
    # Returns type annotated aiobotocore WAFV2 client
    async with session.wafv2.create_client() as wafv2_client:
        wafv2_client: types_aiobotocore_wafv2.client.WAFV2Client
    ```
"""

from __future__ import annotations

from types_aiobotocore_wafv2.client import WAFV2Client

from boto34.aiobotocore.service_factory import ServiceFactory


class WAFV2Service(ServiceFactory[WAFV2Client]):
    SERVICE_NAME = "wafv2"
    _SERVICE_PROP = "wafv2"
