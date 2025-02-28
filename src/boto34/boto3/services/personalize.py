"""
Wrapper for boto3 Personalize service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_personalize/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_personalize.client import PersonalizeClient

from boto34.boto3.service_factory import ServiceFactory


class PersonalizeService(ServiceFactory[PersonalizeClient]):
    """
    Personalize service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_personalize/)
    """
