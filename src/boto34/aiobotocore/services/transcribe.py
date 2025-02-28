"""
Wrapper for aiobotocore TranscribeService service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_transcribe/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_transcribe.client import TranscribeServiceClient

from boto34.aiobotocore.service_factory import ServiceFactory


class TranscribeServiceService(ServiceFactory[TranscribeServiceClient]):
    """
    TranscribeService service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_transcribe/)
    """
