"""
Wrapper for aioboto3 WAFV2 service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_wafv2/)

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
    # Returns type annotated aioboto3 WAFV2 client
    wafv2_client = session.wafv2.client()
    wafv2_client: types_aiobotocore_wafv2.client.WAFV2Client
    ```
"""

from __future__ import annotations

from types_aiobotocore_wafv2.client import WAFV2Client

from boto34.aioboto3.service_factory import ServiceFactory


class WAFV2Service(ServiceFactory[WAFV2Client]):
    SERVICE_NAME = "wafv2"
    _SERVICE_PROP = "wafv2"
