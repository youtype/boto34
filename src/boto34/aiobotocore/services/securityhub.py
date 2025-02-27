"""
Wrapper for aiobotocore SecurityHub service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_securityhub/)

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
    # Returns type annotated aiobotocore SecurityHub client
    async with session.securityhub.create_client() as securityhub_client:
        securityhub_client: types_aiobotocore_securityhub.client.SecurityHubClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_securityhub.client import SecurityHubClient
except ImportError:
    SecurityHubClient = object  # type: ignore[misc,assignment]


class SecurityHubService(
    ServiceFactory[SecurityHubClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "securityhub"
    _SERVICE_PROP = "securityhub"
