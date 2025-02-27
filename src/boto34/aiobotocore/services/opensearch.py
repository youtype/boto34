"""
Wrapper for aiobotocore OpenSearchService service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore OpenSearchService client
    async with session.opensearch.create_client() as opensearch_client:
        opensearch_client: types_aiobotocore_opensearch.client.OpenSearchServiceClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_opensearch.client import OpenSearchServiceClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_opensearch.client import OpenSearchServiceClient
except ImportError:
    OpenSearchServiceClient = object  # type: ignore[misc,assignment]


class OpenSearchServiceService(
    ServiceFactory[OpenSearchServiceClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "opensearch"
    _SERVICE_PROP = "opensearch"
