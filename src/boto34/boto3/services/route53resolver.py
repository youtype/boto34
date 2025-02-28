"""
Wrapper for boto3 Route53Resolver service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_route53resolver/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_route53resolver.client import Route53ResolverClient

from boto34.boto3.service_factory import ServiceFactory


class Route53ResolverService(ServiceFactory[Route53ResolverClient]):
    """
    Route53Resolver service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_route53resolver/)
    """
