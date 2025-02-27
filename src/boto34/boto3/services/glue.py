"""
Wrapper for boto3 Glue service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_glue/)

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
    # Returns type annotated boto3 Glue client
    glue_client = session.glue.client()
    glue_client: types_boto3_glue.client.GlueClient
    ```
"""

from __future__ import annotations

from types_boto3_glue.client import GlueClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_glue.client import GlueClient
except ImportError:
    GlueClient = object  # type: ignore[misc,assignment]


class GlueService(
    ServiceFactory[GlueClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "glue"
    _SERVICE_PROP = "glue"
