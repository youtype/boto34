"""
Wrapper for boto3 Route53Profiles service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_route53profiles/)

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
    # Returns type annotated boto3 Route53Profiles client
    route53profiles_client = session.route53profiles.client()
    route53profiles_client: types_boto3_route53profiles.client.Route53ProfilesClient
    ```
"""

from __future__ import annotations

from types_boto3_route53profiles.client import Route53ProfilesClient

from boto34.boto3.service_factory import ServiceFactory


class Route53ProfilesService(ServiceFactory[Route53ProfilesClient]):
    SERVICE_NAME = "route53profiles"
    _SERVICE_PROP = "route53profiles"
