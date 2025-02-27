"""
Wrapper for aioboto3 SSO service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_sso/)

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
    # Returns type annotated aioboto3 SSO client
    sso_client = session.sso.client()
    sso_client: types_aiobotocore_sso.client.SSOClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_sso.client import SSOClient
except ImportError:
    SSOClient = object  # type: ignore[misc,assignment]


class SSOService(
    ServiceFactory[SSOClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "sso"
    _SERVICE_PROP = "sso"
