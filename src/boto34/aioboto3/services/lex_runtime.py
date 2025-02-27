"""
Wrapper for aioboto3 LexRuntimeService service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_lex_runtime/)

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
    # Returns type annotated aioboto3 LexRuntimeService client
    lex_runtime_client = session.lex_runtime.client()
    lex_runtime_client: types_aiobotocore_lex_runtime.client.LexRuntimeServiceClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_lex_runtime.client import LexRuntimeServiceClient

from boto34.aioboto3.service_factory import ServiceFactory


class LexRuntimeServiceService(ServiceFactory[LexRuntimeServiceClient]):
    SERVICE_NAME = "lex-runtime"
    _SERVICE_PROP = "lex_runtime"
