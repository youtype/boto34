"""
Wrapper for aioboto3 Route53Domains service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_route53domains/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aioboto3 import Session

    # Wrapper for aioboto3.Session constructor
    # Returns boto34.Session inherited from aioboto3.Session
    session = Session()
    session: boto34.aioboto3.session.Session

    # Type annotated aioboto3.Client
    # Uses the same arguments as aioboto3.client method
    # Returns type annotated aioboto3 Route53Domains client
    route53domains_client = session.route53domains.client()
    route53domains_client: types_aiobotocore_route53domains.client.Route53DomainsClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_route53domains.client import Route53DomainsClient

from boto34.aioboto3.service_factory import ServiceFactory


class Route53DomainsService(ServiceFactory[Route53DomainsClient]):
    SERVICE_NAME = "route53domains"
    _SERVICE_PROP = "route53domains"
