"""
Wrapper for aiobotocore Glacier service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_glacier/)

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
    # Returns type annotated aiobotocore Glacier client
    async with session.glacier.create_client() as glacier_client:
        glacier_client: types_aiobotocore_glacier.client.GlacierClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_glacier.client import GlacierClient

from boto34.aiobotocore.service_factory import ServiceFactory


class GlacierService(ServiceFactory[GlacierClient]):
    SERVICE_NAME = "glacier"
    _SERVICE_PROP = "glacier"
