"""
Wrapper for boto3 Route53Resolver service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_route53resolver/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.boto3 import Session

    # Wrapper for boto3.Session constructor
    # Returns boto34.Session inherited from boto3.Session
    session = Session()
    session: boto34.boto3.session.Session

    # Type annotated boto3.Client
    # Uses the same arguments as boto3.client method
    # Returns type annotated boto3 Route53Resolver client
    route53resolver_client = session.route53resolver.client()
    route53resolver_client: types_boto3_route53resolver.client.Route53ResolverClient
    ```
"""

from __future__ import annotations

from types_boto3_route53resolver.client import Route53ResolverClient

from boto34.boto3.service_factory import ServiceFactory


class Route53ResolverService(ServiceFactory[Route53ResolverClient]):
    SERVICE_NAME = "route53resolver"
    _SERVICE_PROP = "route53resolver"
