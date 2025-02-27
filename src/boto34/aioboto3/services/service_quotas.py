"""
Wrapper for aioboto3 ServiceQuotas service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_service_quotas/)

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
    # Returns type annotated aioboto3 ServiceQuotas client
    service_quotas_client = session.service_quotas.client()
    service_quotas_client: types_aiobotocore_service_quotas.client.ServiceQuotasClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_service_quotas.client import ServiceQuotasClient

from boto34.aioboto3.service_factory import ServiceFactory


class ServiceQuotasService(ServiceFactory[ServiceQuotasClient]):
    SERVICE_NAME = "service-quotas"
    _SERVICE_PROP = "service_quotas"
