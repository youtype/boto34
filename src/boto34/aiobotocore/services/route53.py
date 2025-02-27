"""
Wrapper for aiobotocore Route53 service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_route53/)

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
    # Returns type annotated aiobotocore Route53 client
    async with session.route53.create_client() as route53_client:
        route53_client: types_aiobotocore_route53.client.Route53Client
    ```
"""

from __future__ import annotations

from types_aiobotocore_route53.client import Route53Client

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_route53.client import Route53Client
except ImportError:
    Route53Client = object  # type: ignore[misc,assignment]


class Route53Service(
    ServiceFactory[Route53Client]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "route53"
    _SERVICE_PROP = "route53"
