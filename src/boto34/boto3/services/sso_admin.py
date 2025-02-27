"""
Wrapper for boto3 SSOAdmin service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_sso_admin/)

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
    # Returns type annotated boto3 SSOAdmin client
    sso_admin_client = session.sso_admin.client()
    sso_admin_client: types_boto3_sso_admin.client.SSOAdminClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_sso_admin.client import SSOAdminClient
except ImportError:
    SSOAdminClient = object  # type: ignore[misc,assignment]


class SSOAdminService(
    ServiceFactory[SSOAdminClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "sso-admin"
    _SERVICE_PROP = "sso_admin"
