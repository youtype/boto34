"""
Wrapper for aioboto3 Schemas service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_schemas/)

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
    # Returns type annotated aioboto3 Schemas client
    schemas_client = session.schemas.client()
    schemas_client: types_aiobotocore_schemas.client.SchemasClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_schemas.client import SchemasClient
except ImportError:
    SchemasClient = object  # type: ignore[misc,assignment]


class SchemasService(
    ServiceFactory[SchemasClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "schemas"
    _SERVICE_PROP = "schemas"
