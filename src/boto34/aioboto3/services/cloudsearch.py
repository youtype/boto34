"""
Wrapper for aioboto3 CloudSearch service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_cloudsearch/)

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
    # Returns type annotated aioboto3 CloudSearch client
    cloudsearch_client = session.cloudsearch.client()
    cloudsearch_client: types_aiobotocore_cloudsearch.client.CloudSearchClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_cloudsearch.client import CloudSearchClient
except ImportError:
    CloudSearchClient = object  # type: ignore[misc,assignment]


class CloudSearchService(
    ServiceFactory[CloudSearchClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "cloudsearch"
    _SERVICE_PROP = "cloudsearch"
