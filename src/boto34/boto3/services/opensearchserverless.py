"""
Wrapper for boto3 OpenSearchServiceServerless service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_opensearchserverless/)

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
    # Returns type annotated boto3 OpenSearchServiceServerless client
    opensearchserverless_client = session.opensearchserverless.client()
    opensearchserverless_client: (
        types_boto3_opensearchserverless.client.OpenSearchServiceServerlessClient
    )
    ```
"""

from __future__ import annotations

from types_boto3_opensearchserverless.client import OpenSearchServiceServerlessClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_opensearchserverless.client import OpenSearchServiceServerlessClient
except ImportError:
    OpenSearchServiceServerlessClient = object  # type: ignore[misc,assignment]


class OpenSearchServiceServerlessService(
    ServiceFactory[OpenSearchServiceServerlessClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "opensearchserverless"
    _SERVICE_PROP = "opensearchserverless"
