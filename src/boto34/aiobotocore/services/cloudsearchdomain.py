"""
Wrapper for aiobotocore CloudSearchDomain service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudsearchdomain/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_cloudsearchdomain.client import CloudSearchDomainClient

from boto34.aiobotocore.service_factory import ServiceFactory


class CloudSearchDomainService(ServiceFactory[CloudSearchDomainClient]):
    """
    CloudSearchDomain service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudsearchdomain/)
    """
