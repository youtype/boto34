"""
Wrapper for boto3 SSO service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_sso/)

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
    # Returns type annotated boto3 SSO client
    sso_client = session.sso.client()
    sso_client: types_boto3_sso.client.SSOClient
    ```
"""

from __future__ import annotations

from types_boto3_sso.client import SSOClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_sso.client import SSOClient
except ImportError:
    SSOClient = object  # type: ignore[misc,assignment]


class SSOService(
    ServiceFactory[SSOClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "sso"
    _SERVICE_PROP = "sso"
