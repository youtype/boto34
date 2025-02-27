"""
Wrapper for boto3 ServiceQuotas service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_service_quotas/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.boto3 import Session

    # Wrapper for boto3.Session constructor
    # Returns boto34.Session inherited from boto3.Session
    session = Session()
    session: boto34.boto3.session.Session

    # Type annotated boto3.Client
    # Uses the same arguments as boto3.client method
    # Returns type annotated boto3 ServiceQuotas client
    service_quotas_client = session.service_quotas.client()
    service_quotas_client: types_boto3_service_quotas.client.ServiceQuotasClient
    ```
"""

from __future__ import annotations

from types_boto3_service_quotas.client import ServiceQuotasClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_service_quotas.client import ServiceQuotasClient
except ImportError:
    ServiceQuotasClient = object  # type: ignore[misc,assignment]


class ServiceQuotasService(
    ServiceFactory[ServiceQuotasClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "service-quotas"
    _SERVICE_PROP = "service_quotas"
