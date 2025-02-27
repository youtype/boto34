"""
Wrapper for boto3 CloudWatchRUM service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_rum/)

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
    # Returns type annotated boto3 CloudWatchRUM client
    rum_client = session.rum.client()
    rum_client: types_boto3_rum.client.CloudWatchRUMClient
    ```
"""

from __future__ import annotations

from types_boto3_rum.client import CloudWatchRUMClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_rum.client import CloudWatchRUMClient
except ImportError:
    CloudWatchRUMClient = object  # type: ignore[misc,assignment]


class CloudWatchRUMService(
    ServiceFactory[CloudWatchRUMClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "rum"
    _SERVICE_PROP = "rum"
