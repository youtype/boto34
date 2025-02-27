"""
Wrapper for aioboto3 DLM service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_dlm/)

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
    # Returns type annotated aioboto3 DLM client
    dlm_client = session.dlm.client()
    dlm_client: types_aiobotocore_dlm.client.DLMClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_dlm.client import DLMClient
except ImportError:
    DLMClient = object  # type: ignore[misc,assignment]


class DLMService(
    ServiceFactory[DLMClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "dlm"
    _SERVICE_PROP = "dlm"
