"""
Wrapper for aiobotocore Route53Resolver service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_route53resolver/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore Route53Resolver client
    async with session.route53resolver.create_client() as route53resolver_client:
        route53resolver_client: types_aiobotocore_route53resolver.client.Route53ResolverClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_route53resolver.client import Route53ResolverClient
except ImportError:
    Route53ResolverClient = object  # type: ignore[misc,assignment]


class Route53ResolverService(
    ServiceFactory[Route53ResolverClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "route53resolver"
    _SERVICE_PROP = "route53resolver"
