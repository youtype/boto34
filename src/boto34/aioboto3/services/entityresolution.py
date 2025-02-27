"""
Wrapper for aioboto3 EntityResolution service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_entityresolution/)

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
    # Returns type annotated aioboto3 EntityResolution client
    entityresolution_client = session.entityresolution.client()
    entityresolution_client: types_aiobotocore_entityresolution.client.EntityResolutionClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_entityresolution.client import EntityResolutionClient
except ImportError:
    EntityResolutionClient = object  # type: ignore[misc,assignment]


class EntityResolutionService(
    ServiceFactory[EntityResolutionClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "entityresolution"
    _SERVICE_PROP = "entityresolution"
