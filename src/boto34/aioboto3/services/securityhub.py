"""
Wrapper for aioboto3 SecurityHub service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_securityhub/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_securityhub.client import SecurityHubClient

from boto34.aioboto3.service_factory import ServiceFactory


class SecurityHubService(ServiceFactory[SecurityHubClient]):
    """
    SecurityHub service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_securityhub/)
    """
