"""
Wrapper for aiobotocore MigrationHub service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mgh/)

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
    # Returns type annotated aiobotocore MigrationHub client
    async with session.mgh.create_client() as mgh_client:
        mgh_client: types_aiobotocore_mgh.client.MigrationHubClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_mgh.client import MigrationHubClient
except ImportError:
    MigrationHubClient = object  # type: ignore[misc,assignment]


class MigrationHubService(
    ServiceFactory[MigrationHubClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "mgh"
    _SERVICE_PROP = "mgh"
