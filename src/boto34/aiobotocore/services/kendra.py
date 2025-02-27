"""
Wrapper for aiobotocore Kendra service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kendra/)

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
    # Returns type annotated aiobotocore Kendra client
    async with session.kendra.create_client() as kendra_client:
        kendra_client: types_aiobotocore_kendra.client.KendraClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_kendra.client import KendraClient

from boto34.aiobotocore.service_factory import ServiceFactory


class KendraService(ServiceFactory[KendraClient]):
    SERVICE_NAME = "kendra"
    _SERVICE_PROP = "kendra"
