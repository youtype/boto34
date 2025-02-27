"""
Wrapper for aioboto3 Route53Profiles service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_route53profiles/)

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
    # Returns type annotated aioboto3 Route53Profiles client
    route53profiles_client = session.route53profiles.client()
    route53profiles_client: types_aiobotocore_route53profiles.client.Route53ProfilesClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_route53profiles.client import Route53ProfilesClient

from boto34.aioboto3.service_factory import ServiceFactory


class Route53ProfilesService(ServiceFactory[Route53ProfilesClient]):
    SERVICE_NAME = "route53profiles"
    _SERVICE_PROP = "route53profiles"
