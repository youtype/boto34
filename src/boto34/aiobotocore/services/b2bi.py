"""
Wrapper for aiobotocore B2BI service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_b2bi/)

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
    # Returns type annotated aiobotocore B2BI client
    async with session.b2bi.create_client() as b2bi_client:
        b2bi_client: types_aiobotocore_b2bi.client.B2BIClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_b2bi.client import B2BIClient

from boto34.aiobotocore.service_factory import ServiceFactory


class B2BIService(ServiceFactory[B2BIClient]):
    SERVICE_NAME = "b2bi"
    _SERVICE_PROP = "b2bi"
