"""
Wrapper for aioboto3 TrustedAdvisorPublicAPI service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_trustedadvisor/)

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
    # Returns type annotated aioboto3 TrustedAdvisorPublicAPI client
    trustedadvisor_client = session.trustedadvisor.client()
    trustedadvisor_client: types_aiobotocore_trustedadvisor.client.TrustedAdvisorPublicAPIClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_trustedadvisor.client import TrustedAdvisorPublicAPIClient
except ImportError:
    TrustedAdvisorPublicAPIClient = object  # type: ignore[misc,assignment]


class TrustedAdvisorPublicAPIService(
    ServiceFactory[TrustedAdvisorPublicAPIClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "trustedadvisor"
    _SERVICE_PROP = "trustedadvisor"
