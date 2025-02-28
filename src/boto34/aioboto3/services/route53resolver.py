"""
Wrapper for aioboto3 Route53Resolver service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_route53resolver/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_route53resolver.client import Route53ResolverClient

from boto34.aioboto3.service_factory import ServiceFactory


class Route53ResolverService(ServiceFactory[Route53ResolverClient]):
    """
    Route53Resolver service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_route53resolver/)
    """
