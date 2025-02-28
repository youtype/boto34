"""
Wrapper for aioboto3 ServiceQuotas service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_service_quotas/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_service_quotas.client import ServiceQuotasClient

from boto34.aioboto3.service_factory import ServiceFactory


class ServiceQuotasService(ServiceFactory[ServiceQuotasClient]):
    """
    ServiceQuotas service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_service_quotas/)
    """
