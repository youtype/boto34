"""
Wrapper for aiobotocore SSOOIDC service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_oidc/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore SSOOIDC client
    async with session.sso_oidc.create_client() as sso_oidc_client:
        sso_oidc_client: types_aiobotocore_sso_oidc.client.SSOOIDCClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_sso_oidc.client import SSOOIDCClient
except ImportError:
    SSOOIDCClient = object  # type: ignore[misc,assignment]


class SSOOIDCService(
    ServiceFactory[SSOOIDCClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "sso-oidc"
    _SERVICE_PROP = "sso_oidc"
