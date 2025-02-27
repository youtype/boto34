"""
Wrapper for aiobotocore SecurityLake service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_securitylake/)

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
    # Returns type annotated aiobotocore SecurityLake client
    async with session.securitylake.create_client() as securitylake_client:
        securitylake_client: types_aiobotocore_securitylake.client.SecurityLakeClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_securitylake.client import SecurityLakeClient

from boto34.aiobotocore.service_factory import ServiceFactory


class SecurityLakeService(ServiceFactory[SecurityLakeClient]):
    SERVICE_NAME = "securitylake"
    _SERVICE_PROP = "securitylake"
