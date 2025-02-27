"""
Wrapper for aiobotocore Route53Profiles service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_route53profiles/)

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
    # Returns type annotated aiobotocore Route53Profiles client
    async with session.route53profiles.create_client() as route53profiles_client:
        route53profiles_client: types_aiobotocore_route53profiles.client.Route53ProfilesClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_route53profiles.client import Route53ProfilesClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_route53profiles.client import Route53ProfilesClient
except ImportError:
    Route53ProfilesClient = object  # type: ignore[misc,assignment]


class Route53ProfilesService(
    ServiceFactory[Route53ProfilesClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "route53profiles"
    _SERVICE_PROP = "route53profiles"
