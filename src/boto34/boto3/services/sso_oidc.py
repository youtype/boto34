"""
Wrapper for boto3 SSOOIDC service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_sso_oidc/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.boto3 import Session

    # Wrapper for boto3.Session constructor
    # Returns boto34.Session inherited from boto3.Session
    session = Session()
    session: boto34.boto3.session.Session

    # Type annotated boto3.Client
    # Uses the same arguments as boto3.client method
    # Returns type annotated boto3 SSOOIDC client
    sso_oidc_client = session.sso_oidc.client()
    sso_oidc_client: types_boto3_sso_oidc.client.SSOOIDCClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_sso_oidc.client import SSOOIDCClient
except ImportError:
    SSOOIDCClient = object  # type: ignore[misc,assignment]


class SSOOIDCService(
    ServiceFactory[SSOOIDCClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "sso-oidc"
    _SERVICE_PROP = "sso_oidc"
