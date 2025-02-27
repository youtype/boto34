"""
Wrapper for aiobotocore CodeCatalyst service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codecatalyst/)

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
    # Returns type annotated aiobotocore CodeCatalyst client
    async with session.codecatalyst.create_client() as codecatalyst_client:
        codecatalyst_client: types_aiobotocore_codecatalyst.client.CodeCatalystClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_codecatalyst.client import CodeCatalystClient

from boto34.aiobotocore.service_factory import ServiceFactory


class CodeCatalystService(ServiceFactory[CodeCatalystClient]):
    SERVICE_NAME = "codecatalyst"
    _SERVICE_PROP = "codecatalyst"
