"""
Wrapper for boto3 Route53Profiles service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_route53profiles/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_route53profiles.client import Route53ProfilesClient

from boto34.boto3.service_factory import ServiceFactory


class Route53ProfilesService(ServiceFactory[Route53ProfilesClient]):
    """
    Route53Profiles service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_route53profiles/)
    """
