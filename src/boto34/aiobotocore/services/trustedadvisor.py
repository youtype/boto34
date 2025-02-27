"""
Wrapper for aiobotocore TrustedAdvisorPublicAPI service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_trustedadvisor/)

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
    # Returns type annotated aiobotocore TrustedAdvisorPublicAPI client
    async with session.trustedadvisor.create_client() as trustedadvisor_client:
        trustedadvisor_client: types_aiobotocore_trustedadvisor.client.TrustedAdvisorPublicAPIClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_trustedadvisor.client import TrustedAdvisorPublicAPIClient
except ImportError:
    TrustedAdvisorPublicAPIClient = object  # type: ignore[misc,assignment]


class TrustedAdvisorPublicAPIService(
    ServiceFactory[TrustedAdvisorPublicAPIClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "trustedadvisor"
    _SERVICE_PROP = "trustedadvisor"
