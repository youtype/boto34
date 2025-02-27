"""
Wrapper for boto3 OpenSearchService service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_opensearch/)

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
    # Returns type annotated boto3 OpenSearchService client
    opensearch_client = session.opensearch.client()
    opensearch_client: types_boto3_opensearch.client.OpenSearchServiceClient
    ```
"""

from __future__ import annotations

from types_boto3_opensearch.client import OpenSearchServiceClient

from boto34.boto3.service_factory import ServiceFactory


class OpenSearchServiceService(ServiceFactory[OpenSearchServiceClient]):
    SERVICE_NAME = "opensearch"
    _SERVICE_PROP = "opensearch"
