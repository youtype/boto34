"""
Wrapper for boto3 SSOOIDC service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_sso_oidc/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_sso_oidc.client import SSOOIDCClient

from boto34.boto3.service_factory import ServiceFactory


class SSOOIDCService(ServiceFactory[SSOOIDCClient]):
    """
    SSOOIDC service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_sso_oidc/)
    """
