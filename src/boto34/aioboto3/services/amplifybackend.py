"""
Wrapper for aioboto3 AmplifyBackend service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_amplifybackend/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_amplifybackend.client import AmplifyBackendClient

from boto34.aioboto3.service_factory import ServiceFactory


class AmplifyBackendService(ServiceFactory[AmplifyBackendClient]):
    """
    AmplifyBackend service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_amplifybackend/)
    """
