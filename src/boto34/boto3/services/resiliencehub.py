"""
Wrapper for boto3 ResilienceHub service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_resiliencehub/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_resiliencehub.client import ResilienceHubClient

from boto34.boto3.service_factory import ServiceFactory


class ResilienceHubService(ServiceFactory[ResilienceHubClient]):
    """
    ResilienceHub service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_resiliencehub/)
    """
