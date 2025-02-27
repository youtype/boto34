"""
Wrapper for aiobotocore EntityResolution service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_entityresolution/)

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
    # Returns type annotated aiobotocore EntityResolution client
    async with session.entityresolution.create_client() as entityresolution_client:
        entityresolution_client: types_aiobotocore_entityresolution.client.EntityResolutionClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_entityresolution.client import EntityResolutionClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_entityresolution.client import EntityResolutionClient
except ImportError:
    EntityResolutionClient = object  # type: ignore[misc,assignment]


class EntityResolutionService(
    ServiceFactory[EntityResolutionClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "entityresolution"
    _SERVICE_PROP = "entityresolution"
