"""
Wrapper for boto3 Organizations service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_organizations/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_organizations.client import OrganizationsClient

from boto34.boto3.service_factory import ServiceFactory


class OrganizationsService(ServiceFactory[OrganizationsClient]):
    """
    Organizations service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_organizations/)
    """
