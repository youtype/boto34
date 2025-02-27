"""
Wrapper for boto3 Route53 service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_route53/)

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
    # Returns type annotated boto3 Route53 client
    route53_client = session.route53.client()
    route53_client: types_boto3_route53.client.Route53Client
    ```
"""

from __future__ import annotations

from types_boto3_route53.client import Route53Client

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_route53.client import Route53Client
except ImportError:
    Route53Client = object  # type: ignore[misc,assignment]


class Route53Service(
    ServiceFactory[Route53Client]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "route53"
    _SERVICE_PROP = "route53"
