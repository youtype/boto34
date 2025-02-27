"""
Wrapper for aioboto3 SSOAdmin service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_sso_admin/)

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
    # Returns type annotated aioboto3 SSOAdmin client
    sso_admin_client = session.sso_admin.client()
    sso_admin_client: types_aiobotocore_sso_admin.client.SSOAdminClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_sso_admin.client import SSOAdminClient

from boto34.aioboto3.service_factory import ServiceFactory


class SSOAdminService(ServiceFactory[SSOAdminClient]):
    SERVICE_NAME = "sso-admin"
    _SERVICE_PROP = "sso_admin"
