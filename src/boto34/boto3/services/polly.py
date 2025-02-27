"""
Wrapper for boto3 Polly service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_polly/)

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
    # Returns type annotated boto3 Polly client
    polly_client = session.polly.client()
    polly_client: types_boto3_polly.client.PollyClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_polly.client import PollyClient
except ImportError:
    PollyClient = object  # type: ignore[misc,assignment]


class PollyService(
    ServiceFactory[PollyClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "polly"
    _SERVICE_PROP = "polly"
