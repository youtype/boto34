"""
Wrapper for boto3 LexRuntimeV2 service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_lexv2_runtime/)

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
    # Returns type annotated boto3 LexRuntimeV2 client
    lexv2_runtime_client = session.lexv2_runtime.client()
    lexv2_runtime_client: types_boto3_lexv2_runtime.client.LexRuntimeV2Client
    ```
"""

from __future__ import annotations

from types_boto3_lexv2_runtime.client import LexRuntimeV2Client

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_lexv2_runtime.client import LexRuntimeV2Client
except ImportError:
    LexRuntimeV2Client = object  # type: ignore[misc,assignment]


class LexRuntimeV2Service(
    ServiceFactory[LexRuntimeV2Client]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "lexv2-runtime"
    _SERVICE_PROP = "lexv2_runtime"
