"""
Wrapper for aiobotocore TranscribeService service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_transcribe/)

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
    # Returns type annotated aiobotocore TranscribeService client
    async with session.transcribe.create_client() as transcribe_client:
        transcribe_client: types_aiobotocore_transcribe.client.TranscribeServiceClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_transcribe.client import TranscribeServiceClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_transcribe.client import TranscribeServiceClient
except ImportError:
    TranscribeServiceClient = object  # type: ignore[misc,assignment]


class TranscribeServiceService(
    ServiceFactory[TranscribeServiceClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "transcribe"
    _SERVICE_PROP = "transcribe"
