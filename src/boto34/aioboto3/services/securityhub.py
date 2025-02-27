"""
Wrapper for aioboto3 SecurityHub service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_securityhub/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aioboto3 import Session

    # Wrapper for aioboto3.Session constructor
    # Returns boto34.Session inherited from aioboto3.Session
    session = Session()
    session: boto34.aioboto3.session.Session

    # Type annotated aioboto3.Client
    # Uses the same arguments as aioboto3.client method
    # Returns type annotated aioboto3 SecurityHub client
    securityhub_client = session.securityhub.client()
    securityhub_client: types_aiobotocore_securityhub.client.SecurityHubClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_securityhub.client import SecurityHubClient
except ImportError:
    SecurityHubClient = object  # type: ignore[misc,assignment]


class SecurityHubService(
    ServiceFactory[SecurityHubClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "securityhub"
    _SERVICE_PROP = "securityhub"
