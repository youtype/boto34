"""
Wrapper for aioboto3 Organizations service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_organizations/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_organizations.client import OrganizationsClient

from boto34.aioboto3.service_factory import ServiceFactory


class OrganizationsService(ServiceFactory[OrganizationsClient]):
    """
    Organizations service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_organizations/)
    """
