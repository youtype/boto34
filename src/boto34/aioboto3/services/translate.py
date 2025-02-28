"""
Wrapper for aioboto3 Translate service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_translate/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_translate.client import TranslateClient

from boto34.aioboto3.service_factory import ServiceFactory


class TranslateService(ServiceFactory[TranslateClient]):
    """
    Translate service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_translate/)
    """
