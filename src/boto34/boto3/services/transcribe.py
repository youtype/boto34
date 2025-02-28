"""
Wrapper for boto3 TranscribeService service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_transcribe/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_transcribe.client import TranscribeServiceClient

from boto34.boto3.service_factory import ServiceFactory


class TranscribeServiceService(ServiceFactory[TranscribeServiceClient]):
    """
    TranscribeService service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_transcribe/)
    """
