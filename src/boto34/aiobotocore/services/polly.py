"""
Wrapper for aiobotocore Polly service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_polly/)

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
    # Returns type annotated aiobotocore Polly client
    async with session.polly.create_client() as polly_client:
        polly_client: types_aiobotocore_polly.client.PollyClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_polly.client import PollyClient

from boto34.aiobotocore.service_factory import ServiceFactory


class PollyService(ServiceFactory[PollyClient]):
    SERVICE_NAME = "polly"
    _SERVICE_PROP = "polly"
