"""
Wrapper for boto3 Schemas service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_schemas/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.boto3 import Session

    # Wrapper for boto3.Session constructor
    # Returns boto34.Session inherited from boto3.Session
    session = Session()
    session: boto34.boto3.session.Session

    # Type annotated boto3.Client
    # Uses the same arguments as boto3.client method
    # Returns type annotated boto3 Schemas client
    schemas_client = session.schemas.client()
    schemas_client: types_boto3_schemas.client.SchemasClient
    ```
"""

from __future__ import annotations

from types_boto3_schemas.client import SchemasClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_schemas.client import SchemasClient
except ImportError:
    SchemasClient = object  # type: ignore[misc,assignment]


class SchemasService(
    ServiceFactory[SchemasClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "schemas"
    _SERVICE_PROP = "schemas"
