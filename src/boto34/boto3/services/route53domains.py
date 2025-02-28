"""
Wrapper for boto3 Route53Domains service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_route53domains/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_route53domains.client import Route53DomainsClient

from boto34.boto3.service_factory import ServiceFactory


class Route53DomainsService(ServiceFactory[Route53DomainsClient]):
    """
    Route53Domains service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_route53domains/)
    """
