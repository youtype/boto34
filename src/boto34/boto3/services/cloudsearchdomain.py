"""
Wrapper for boto3 CloudSearchDomain service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cloudsearchdomain/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_cloudsearchdomain.client import CloudSearchDomainClient

from boto34.boto3.service_factory import ServiceFactory


class CloudSearchDomainService(ServiceFactory[CloudSearchDomainClient]):
    """
    CloudSearchDomain service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cloudsearchdomain/)
    """
