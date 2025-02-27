"""
Wrapper for aiobotocore LexRuntimeService service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lex_runtime/)

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
    # Returns type annotated aiobotocore LexRuntimeService client
    async with session.lex_runtime.create_client() as lex_runtime_client:
        lex_runtime_client: types_aiobotocore_lex_runtime.client.LexRuntimeServiceClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_lex_runtime.client import LexRuntimeServiceClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_lex_runtime.client import LexRuntimeServiceClient
except ImportError:
    LexRuntimeServiceClient = object  # type: ignore[misc,assignment]


class LexRuntimeServiceService(
    ServiceFactory[LexRuntimeServiceClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "lex-runtime"
    _SERVICE_PROP = "lex_runtime"
