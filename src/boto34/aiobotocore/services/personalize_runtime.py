"""
Wrapper for aiobotocore PersonalizeRuntime service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_personalize_runtime/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_personalize_runtime.client import PersonalizeRuntimeClient

from boto34.aiobotocore.service_factory import ServiceFactory


class PersonalizeRuntimeService(ServiceFactory[PersonalizeRuntimeClient]):
    """
    PersonalizeRuntime service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_personalize_runtime/)
    """
