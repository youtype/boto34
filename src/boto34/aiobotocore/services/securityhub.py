"""
Wrapper for aiobotocore SecurityHub service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_securityhub/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_securityhub.client import SecurityHubClient

from boto34.aiobotocore.service_factory import ServiceFactory


class SecurityHubService(ServiceFactory[SecurityHubClient]):
    """
    SecurityHub service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_securityhub/)
    """
