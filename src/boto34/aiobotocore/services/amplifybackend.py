"""
Wrapper for aiobotocore AmplifyBackend service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amplifybackend/)

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
    # Returns type annotated aiobotocore AmplifyBackend client
    async with session.amplifybackend.create_client() as amplifybackend_client:
        amplifybackend_client: types_aiobotocore_amplifybackend.client.AmplifyBackendClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_amplifybackend.client import AmplifyBackendClient
except ImportError:
    AmplifyBackendClient = object  # type: ignore[misc,assignment]


class AmplifyBackendService(
    ServiceFactory[AmplifyBackendClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "amplifybackend"
    _SERVICE_PROP = "amplifybackend"
