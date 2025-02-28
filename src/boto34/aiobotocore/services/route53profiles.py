"""
Wrapper for aiobotocore Route53Profiles service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_route53profiles/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_route53profiles.client import Route53ProfilesClient

from boto34.aiobotocore.service_factory import ServiceFactory


class Route53ProfilesService(ServiceFactory[Route53ProfilesClient]):
    """
    Route53Profiles service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_route53profiles/)
    """
