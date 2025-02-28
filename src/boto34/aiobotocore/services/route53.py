"""
Wrapper for aiobotocore Route53 service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_route53/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_route53.client import Route53Client

from boto34.aiobotocore.service_factory import ServiceFactory


class Route53Service(ServiceFactory[Route53Client]):
    """
    Route53 service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_route53/)
    """
