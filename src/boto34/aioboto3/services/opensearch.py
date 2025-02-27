"""
Wrapper for aioboto3 OpenSearchService service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_opensearch/)

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
    # Returns type annotated aioboto3 OpenSearchService client
    opensearch_client = session.opensearch.client()
    opensearch_client: types_aiobotocore_opensearch.client.OpenSearchServiceClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_opensearch.client import OpenSearchServiceClient

from boto34.aioboto3.service_factory import ServiceFactory


class OpenSearchServiceService(ServiceFactory[OpenSearchServiceClient]):
    SERVICE_NAME = "opensearch"
    _SERVICE_PROP = "opensearch"
