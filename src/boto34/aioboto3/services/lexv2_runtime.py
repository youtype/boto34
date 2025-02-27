"""
Wrapper for aioboto3 LexRuntimeV2 service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_lexv2_runtime/)

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
    # Returns type annotated aioboto3 LexRuntimeV2 client
    lexv2_runtime_client = session.lexv2_runtime.client()
    lexv2_runtime_client: types_aiobotocore_lexv2_runtime.client.LexRuntimeV2Client
    ```
"""

from __future__ import annotations

from types_aiobotocore_lexv2_runtime.client import LexRuntimeV2Client

from boto34.aioboto3.service_factory import ServiceFactory


class LexRuntimeV2Service(ServiceFactory[LexRuntimeV2Client]):
    SERVICE_NAME = "lexv2-runtime"
    _SERVICE_PROP = "lexv2_runtime"
