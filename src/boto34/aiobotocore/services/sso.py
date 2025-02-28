"""
Wrapper for aiobotocore SSO service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_sso.client import SSOClient

from boto34.aiobotocore.service_factory import ServiceFactory


class SSOService(ServiceFactory[SSOClient]):
    """
    SSO service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso/)
    """
