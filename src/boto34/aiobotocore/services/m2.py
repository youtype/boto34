"""
Wrapper for aiobotocore MainframeModernization service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_m2/)

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
    # Returns type annotated aiobotocore MainframeModernization client
    async with session.m2.create_client() as m2_client:
        m2_client: types_aiobotocore_m2.client.MainframeModernizationClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_m2.client import MainframeModernizationClient

from boto34.aiobotocore.service_factory import ServiceFactory


class MainframeModernizationService(ServiceFactory[MainframeModernizationClient]):
    SERVICE_NAME = "m2"
    _SERVICE_PROP = "m2"
