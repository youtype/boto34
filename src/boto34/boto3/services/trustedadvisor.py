"""
Wrapper for boto3 TrustedAdvisorPublicAPI service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_trustedadvisor/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_trustedadvisor.client import TrustedAdvisorPublicAPIClient

from boto34.boto3.service_factory import ServiceFactory


class TrustedAdvisorPublicAPIService(ServiceFactory[TrustedAdvisorPublicAPIClient]):
    """
    TrustedAdvisorPublicAPI service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_trustedadvisor/)
    """
