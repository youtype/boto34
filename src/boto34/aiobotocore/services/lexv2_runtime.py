"""
Wrapper for aiobotocore LexRuntimeV2 service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_runtime/)

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
    # Returns type annotated aiobotocore LexRuntimeV2 client
    async with session.lexv2_runtime.create_client() as lexv2_runtime_client:
        lexv2_runtime_client: types_aiobotocore_lexv2_runtime.client.LexRuntimeV2Client
    ```
"""

from __future__ import annotations

from types_aiobotocore_lexv2_runtime.client import LexRuntimeV2Client

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_lexv2_runtime.client import LexRuntimeV2Client
except ImportError:
    LexRuntimeV2Client = object  # type: ignore[misc,assignment]


class LexRuntimeV2Service(
    ServiceFactory[LexRuntimeV2Client]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "lexv2-runtime"
    _SERVICE_PROP = "lexv2_runtime"
