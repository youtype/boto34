"""
Wrapper for boto3 SupportApp service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_support_app/)

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
    # Returns type annotated boto3 SupportApp client
    support_app_client = session.support_app.client()
    support_app_client: types_boto3_support_app.client.SupportAppClient
    ```
"""

from __future__ import annotations

from types_boto3_support_app.client import SupportAppClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_support_app.client import SupportAppClient
except ImportError:
    SupportAppClient = object  # type: ignore[misc,assignment]


class SupportAppService(
    ServiceFactory[SupportAppClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "support-app"
    _SERVICE_PROP = "support_app"
