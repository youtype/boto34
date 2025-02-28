"""
Wrapper for boto3 ServiceQuotas service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_service_quotas/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_service_quotas.client import ServiceQuotasClient

from boto34.boto3.service_factory import ServiceFactory


class ServiceQuotasService(ServiceFactory[ServiceQuotasClient]):
    """
    ServiceQuotas service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_service_quotas/)
    """
