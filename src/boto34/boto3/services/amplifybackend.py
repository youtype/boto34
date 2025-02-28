"""
Wrapper for boto3 AmplifyBackend service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_amplifybackend/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_amplifybackend.client import AmplifyBackendClient

from boto34.boto3.service_factory import ServiceFactory


class AmplifyBackendService(ServiceFactory[AmplifyBackendClient]):
    """
    AmplifyBackend service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_amplifybackend/)
    """
