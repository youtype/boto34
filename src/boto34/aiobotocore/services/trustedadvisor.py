"""
Wrapper for aiobotocore TrustedAdvisorPublicAPI service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_trustedadvisor/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_trustedadvisor.client import TrustedAdvisorPublicAPIClient

from boto34.aiobotocore.service_factory import ServiceFactory


class TrustedAdvisorPublicAPIService(ServiceFactory[TrustedAdvisorPublicAPIClient]):
    """
    TrustedAdvisorPublicAPI service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_trustedadvisor/)
    """
