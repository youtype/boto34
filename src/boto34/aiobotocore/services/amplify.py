"""
Wrapper for aiobotocore Amplify service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amplify/)

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
    # Returns type annotated aiobotocore Amplify client
    async with session.amplify.create_client() as amplify_client:
        amplify_client: types_aiobotocore_amplify.client.AmplifyClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_amplify.client import AmplifyClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_amplify.client import AmplifyClient
except ImportError:
    AmplifyClient = object  # type: ignore[misc,assignment]


class AmplifyService(
    ServiceFactory[AmplifyClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "amplify"
    _SERVICE_PROP = "amplify"
