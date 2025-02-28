"""
Wrapper for boto3 SecurityHub service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_securityhub/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_securityhub.client import SecurityHubClient

from boto34.boto3.service_factory import ServiceFactory


class SecurityHubService(ServiceFactory[SecurityHubClient]):
    """
    SecurityHub service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_securityhub/)
    """
