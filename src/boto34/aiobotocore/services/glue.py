"""
Wrapper for aiobotocore Glue service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_glue/)

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
    # Returns type annotated aiobotocore Glue client
    async with session.glue.create_client() as glue_client:
        glue_client: types_aiobotocore_glue.client.GlueClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_glue.client import GlueClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_glue.client import GlueClient
except ImportError:
    GlueClient = object  # type: ignore[misc,assignment]


class GlueService(
    ServiceFactory[GlueClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "glue"
    _SERVICE_PROP = "glue"
