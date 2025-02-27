"""
Wrapper for aioboto3 GlueDataBrew service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_databrew/)

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
    # Returns type annotated aioboto3 GlueDataBrew client
    databrew_client = session.databrew.client()
    databrew_client: types_aiobotocore_databrew.client.GlueDataBrewClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_databrew.client import GlueDataBrewClient
except ImportError:
    GlueDataBrewClient = object  # type: ignore[misc,assignment]


class GlueDataBrewService(
    ServiceFactory[GlueDataBrewClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "databrew"
    _SERVICE_PROP = "databrew"
