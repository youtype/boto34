"""
Wrapper for aiobotocore OpenSearchIngestion service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_osis/)

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
    # Returns type annotated aiobotocore OpenSearchIngestion client
    async with session.osis.create_client() as osis_client:
        osis_client: types_aiobotocore_osis.client.OpenSearchIngestionClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_osis.client import OpenSearchIngestionClient
except ImportError:
    OpenSearchIngestionClient = object  # type: ignore[misc,assignment]


class OpenSearchIngestionService(
    ServiceFactory[OpenSearchIngestionClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "osis"
    _SERVICE_PROP = "osis"
