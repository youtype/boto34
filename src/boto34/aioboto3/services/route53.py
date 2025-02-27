"""
Wrapper for aioboto3 Route53 service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_route53/)

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
    # Returns type annotated aioboto3 Route53 client
    route53_client = session.route53.client()
    route53_client: types_aiobotocore_route53.client.Route53Client
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_route53.client import Route53Client
except ImportError:
    Route53Client = object  # type: ignore[misc,assignment]


class Route53Service(
    ServiceFactory[Route53Client]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "route53"
    _SERVICE_PROP = "route53"
