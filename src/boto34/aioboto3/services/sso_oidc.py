"""
Wrapper for aioboto3 SSOOIDC service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_sso_oidc/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aioboto3 import Session

    # Wrapper for aioboto3.Session constructor
    # Returns boto34.Session inherited from aioboto3.Session
    session = Session()
    session: boto34.aioboto3.session.Session

    # Type annotated aioboto3.Client
    # Uses the same arguments as aioboto3.client method
    # Returns type annotated aioboto3 SSOOIDC client
    sso_oidc_client = session.sso_oidc.client()
    sso_oidc_client: types_aiobotocore_sso_oidc.client.SSOOIDCClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_sso_oidc.client import SSOOIDCClient
except ImportError:
    SSOOIDCClient = object  # type: ignore[misc,assignment]


class SSOOIDCService(
    ServiceFactory[SSOOIDCClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "sso-oidc"
    _SERVICE_PROP = "sso_oidc"
