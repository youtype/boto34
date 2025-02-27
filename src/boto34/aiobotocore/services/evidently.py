"""
Wrapper for aiobotocore CloudWatchEvidently service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_evidently/)

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
    # Returns type annotated aiobotocore CloudWatchEvidently client
    async with session.evidently.create_client() as evidently_client:
        evidently_client: types_aiobotocore_evidently.client.CloudWatchEvidentlyClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_evidently.client import CloudWatchEvidentlyClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_evidently.client import CloudWatchEvidentlyClient
except ImportError:
    CloudWatchEvidentlyClient = object  # type: ignore[misc,assignment]


class CloudWatchEvidentlyService(
    ServiceFactory[CloudWatchEvidentlyClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "evidently"
    _SERVICE_PROP = "evidently"
