"""
Wrapper for boto3 GlueDataBrew service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_databrew/)

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
    # Returns type annotated boto3 GlueDataBrew client
    databrew_client = session.databrew.client()
    databrew_client: types_boto3_databrew.client.GlueDataBrewClient
    ```
"""

from __future__ import annotations

from types_boto3_databrew.client import GlueDataBrewClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_databrew.client import GlueDataBrewClient
except ImportError:
    GlueDataBrewClient = object  # type: ignore[misc,assignment]


class GlueDataBrewService(
    ServiceFactory[GlueDataBrewClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "databrew"
    _SERVICE_PROP = "databrew"
