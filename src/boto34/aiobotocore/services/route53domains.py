"""
Wrapper for aiobotocore Route53Domains service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_route53domains/)

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
    # Returns type annotated aiobotocore Route53Domains client
    async with session.route53domains.create_client() as route53domains_client:
        route53domains_client: types_aiobotocore_route53domains.client.Route53DomainsClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_route53domains.client import Route53DomainsClient

from boto34.aiobotocore.service_factory import ServiceFactory


class Route53DomainsService(ServiceFactory[Route53DomainsClient]):
    SERVICE_NAME = "route53domains"
    _SERVICE_PROP = "route53domains"
