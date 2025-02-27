"""
Wrapper for boto3 Translate service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_translate/)

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
    # Returns type annotated boto3 Translate client
    translate_client = session.translate.client()
    translate_client: types_boto3_translate.client.TranslateClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_translate.client import TranslateClient
except ImportError:
    TranslateClient = object  # type: ignore[misc,assignment]


class TranslateService(
    ServiceFactory[TranslateClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "translate"
    _SERVICE_PROP = "translate"
