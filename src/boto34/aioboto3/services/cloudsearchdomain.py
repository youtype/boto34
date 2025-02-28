"""
Wrapper for aioboto3 CloudSearchDomain service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_cloudsearchdomain/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_cloudsearchdomain.client import CloudSearchDomainClient

from boto34.aioboto3.service_factory import ServiceFactory


class CloudSearchDomainService(ServiceFactory[CloudSearchDomainClient]):
    """
    CloudSearchDomain service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_cloudsearchdomain/)
    """
