"""
Wrapper for boto3 Translate service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_translate/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_translate.client import TranslateClient

from boto34.boto3.service_factory import ServiceFactory


class TranslateService(ServiceFactory[TranslateClient]):
    """
    Translate service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_translate/)
    """
