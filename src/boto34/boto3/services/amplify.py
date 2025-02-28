"""
Wrapper for boto3 Amplify service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_amplify/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_amplify.client import AmplifyClient

from boto34.boto3.service_factory import ServiceFactory


class AmplifyService(ServiceFactory[AmplifyClient]):
    """
    Amplify service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_amplify/)
    """
