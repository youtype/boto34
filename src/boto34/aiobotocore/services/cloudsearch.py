"""
Wrapper for aiobotocore CloudSearch service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudsearch/)

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
    # Returns type annotated aiobotocore CloudSearch client
    async with session.cloudsearch.create_client() as cloudsearch_client:
        cloudsearch_client: types_aiobotocore_cloudsearch.client.CloudSearchClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_cloudsearch.client import CloudSearchClient
except ImportError:
    CloudSearchClient = object  # type: ignore[misc,assignment]


class CloudSearchService(
    ServiceFactory[CloudSearchClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "cloudsearch"
    _SERVICE_PROP = "cloudsearch"
