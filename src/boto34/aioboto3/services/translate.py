"""
Wrapper for aioboto3 Translate service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_translate/)

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
    # Returns type annotated aioboto3 Translate client
    translate_client = session.translate.client()
    translate_client: types_aiobotocore_translate.client.TranslateClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_translate.client import TranslateClient

from boto34.aioboto3.service_factory import ServiceFactory


class TranslateService(ServiceFactory[TranslateClient]):
    SERVICE_NAME = "translate"
    _SERVICE_PROP = "translate"
