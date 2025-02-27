"""
Wrapper for aiobotocore SSOAdmin service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/)

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
    # Returns type annotated aiobotocore SSOAdmin client
    async with session.sso_admin.create_client() as sso_admin_client:
        sso_admin_client: types_aiobotocore_sso_admin.client.SSOAdminClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_sso_admin.client import SSOAdminClient
except ImportError:
    SSOAdminClient = object  # type: ignore[misc,assignment]


class SSOAdminService(
    ServiceFactory[SSOAdminClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "sso-admin"
    _SERVICE_PROP = "sso_admin"
