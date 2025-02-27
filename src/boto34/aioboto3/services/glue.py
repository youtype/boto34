"""
Wrapper for aioboto3 Glue service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_glue/)

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
    # Returns type annotated aioboto3 Glue client
    glue_client = session.glue.client()
    glue_client: types_aiobotocore_glue.client.GlueClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_glue.client import GlueClient

from boto34.aioboto3.service_factory import ServiceFactory


class GlueService(ServiceFactory[GlueClient]):
    SERVICE_NAME = "glue"
    _SERVICE_PROP = "glue"
