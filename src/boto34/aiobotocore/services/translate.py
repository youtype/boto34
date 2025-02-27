"""
Wrapper for aiobotocore Translate service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_translate/)

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
    # Returns type annotated aiobotocore Translate client
    async with session.translate.create_client() as translate_client:
        translate_client: types_aiobotocore_translate.client.TranslateClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_translate.client import TranslateClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_translate.client import TranslateClient
except ImportError:
    TranslateClient = object  # type: ignore[misc,assignment]


class TranslateService(
    ServiceFactory[TranslateClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "translate"
    _SERVICE_PROP = "translate"
