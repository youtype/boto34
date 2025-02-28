"""
Wrapper for aiobotocore SSOOIDC service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_oidc/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_sso_oidc.client import SSOOIDCClient

from boto34.aiobotocore.service_factory import ServiceFactory


class SSOOIDCService(ServiceFactory[SSOOIDCClient]):
    """
    SSOOIDC service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_oidc/)
    """
