"""
Wrapper for aioboto3 LexRuntimeService service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_lex_runtime/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_lex_runtime.client import LexRuntimeServiceClient

from boto34.aioboto3.service_factory import ServiceFactory


class LexRuntimeServiceService(ServiceFactory[LexRuntimeServiceClient]):
    """
    LexRuntimeService service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_lex_runtime/)
    """
