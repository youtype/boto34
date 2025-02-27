"""
Wrapper for aiobotocore ServiceQuotas service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_service_quotas/)

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
    # Returns type annotated aiobotocore ServiceQuotas client
    async with session.service_quotas.create_client() as service_quotas_client:
        service_quotas_client: types_aiobotocore_service_quotas.client.ServiceQuotasClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_service_quotas.client import ServiceQuotasClient
except ImportError:
    ServiceQuotasClient = object  # type: ignore[misc,assignment]


class ServiceQuotasService(
    ServiceFactory[ServiceQuotasClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "service-quotas"
    _SERVICE_PROP = "service_quotas"
