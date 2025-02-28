"""
Wrapper for boto3 Route53 service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_route53/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_route53.client import Route53Client

from boto34.boto3.service_factory import ServiceFactory


class Route53Service(ServiceFactory[Route53Client]):
    """
    Route53 service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_route53/)
    """
