"""
Wrapper for boto3 PersonalizeRuntime service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_personalize_runtime/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_personalize_runtime.client import PersonalizeRuntimeClient

from boto34.boto3.service_factory import ServiceFactory


class PersonalizeRuntimeService(ServiceFactory[PersonalizeRuntimeClient]):
    """
    PersonalizeRuntime service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_personalize_runtime/)
    """
