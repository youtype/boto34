"""
Wrapper for aiobotocore Support service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_support/)

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
    # Returns type annotated aiobotocore Support client
    async with session.support.create_client() as support_client:
        support_client: types_aiobotocore_support.client.SupportClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_support.client import SupportClient

from boto34.aiobotocore.service_factory import ServiceFactory


class SupportService(ServiceFactory[SupportClient]):
    SERVICE_NAME = "support"
    _SERVICE_PROP = "support"
