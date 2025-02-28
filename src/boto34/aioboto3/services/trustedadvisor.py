"""
Wrapper for aioboto3 TrustedAdvisorPublicAPI service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_trustedadvisor/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_trustedadvisor.client import TrustedAdvisorPublicAPIClient

from boto34.aioboto3.service_factory import ServiceFactory


class TrustedAdvisorPublicAPIService(ServiceFactory[TrustedAdvisorPublicAPIClient]):
    """
    TrustedAdvisorPublicAPI service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_trustedadvisor/)
    """
