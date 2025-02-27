"""
Wrapper for boto3 LexRuntimeService service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_lex_runtime/)

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
    # Returns type annotated boto3 LexRuntimeService client
    lex_runtime_client = session.lex_runtime.client()
    lex_runtime_client: types_boto3_lex_runtime.client.LexRuntimeServiceClient
    ```
"""

from __future__ import annotations

from types_boto3_lex_runtime.client import LexRuntimeServiceClient

from boto34.boto3.service_factory import ServiceFactory


class LexRuntimeServiceService(ServiceFactory[LexRuntimeServiceClient]):
    SERVICE_NAME = "lex-runtime"
    _SERVICE_PROP = "lex_runtime"
