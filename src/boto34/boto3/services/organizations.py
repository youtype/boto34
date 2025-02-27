"""
Wrapper for boto3 Organizations service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_organizations/)

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
    # Returns type annotated boto3 Organizations client
    organizations_client = session.organizations.client()
    organizations_client: types_boto3_organizations.client.OrganizationsClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_organizations.client import OrganizationsClient
except ImportError:
    OrganizationsClient = object  # type: ignore[misc,assignment]


class OrganizationsService(
    ServiceFactory[OrganizationsClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "organizations"
    _SERVICE_PROP = "organizations"
