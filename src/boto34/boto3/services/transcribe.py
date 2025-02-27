"""
Wrapper for boto3 TranscribeService service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_transcribe/)

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
    # Returns type annotated boto3 TranscribeService client
    transcribe_client = session.transcribe.client()
    transcribe_client: types_boto3_transcribe.client.TranscribeServiceClient
    ```
"""

from __future__ import annotations

from types_boto3_transcribe.client import TranscribeServiceClient

from boto34.boto3.service_factory import ServiceFactory


class TranscribeServiceService(ServiceFactory[TranscribeServiceClient]):
    SERVICE_NAME = "transcribe"
    _SERVICE_PROP = "transcribe"
