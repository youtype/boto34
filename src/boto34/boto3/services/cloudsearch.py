"""
Wrapper for boto3 CloudSearch service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cloudsearch/)

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
    # Returns type annotated boto3 CloudSearch client
    cloudsearch_client = session.cloudsearch.client()
    cloudsearch_client: types_boto3_cloudsearch.client.CloudSearchClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_cloudsearch.client import CloudSearchClient
except ImportError:
    CloudSearchClient = object  # type: ignore[misc,assignment]


class CloudSearchService(
    ServiceFactory[CloudSearchClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "cloudsearch"
    _SERVICE_PROP = "cloudsearch"
