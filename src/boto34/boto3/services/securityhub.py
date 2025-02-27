"""
Wrapper for boto3 SecurityHub service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_securityhub/)

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
    # Returns type annotated boto3 SecurityHub client
    securityhub_client = session.securityhub.client()
    securityhub_client: types_boto3_securityhub.client.SecurityHubClient
    ```
"""

from __future__ import annotations

from types_boto3_securityhub.client import SecurityHubClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_securityhub.client import SecurityHubClient
except ImportError:
    SecurityHubClient = object  # type: ignore[misc,assignment]


class SecurityHubService(
    ServiceFactory[SecurityHubClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "securityhub"
    _SERVICE_PROP = "securityhub"
