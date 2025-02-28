"""
Wrapper for aioboto3 Personalize service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_personalize/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_personalize.client import PersonalizeClient

from boto34.aioboto3.service_factory import ServiceFactory


class PersonalizeService(ServiceFactory[PersonalizeClient]):
    """
    Personalize service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_personalize/)
    """
