"""
Wrapper for aiobotocore DLM service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dlm/)

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
    # Returns type annotated aiobotocore DLM client
    async with session.dlm.create_client() as dlm_client:
        dlm_client: types_aiobotocore_dlm.client.DLMClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_dlm.client import DLMClient
except ImportError:
    DLMClient = object  # type: ignore[misc,assignment]


class DLMService(
    ServiceFactory[DLMClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "dlm"
    _SERVICE_PROP = "dlm"
