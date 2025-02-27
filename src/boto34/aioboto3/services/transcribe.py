"""
Wrapper for aioboto3 TranscribeService service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_transcribe/)

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
    # Returns type annotated aioboto3 TranscribeService client
    transcribe_client = session.transcribe.client()
    transcribe_client: types_aiobotocore_transcribe.client.TranscribeServiceClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_transcribe.client import TranscribeServiceClient

from boto34.aioboto3.service_factory import ServiceFactory


class TranscribeServiceService(ServiceFactory[TranscribeServiceClient]):
    SERVICE_NAME = "transcribe"
    _SERVICE_PROP = "transcribe"
