"""
Wrapper for aioboto3 Organizations service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_organizations/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aioboto3 import Session

    # Wrapper for aioboto3.Session constructor
    # Returns boto34.Session inherited from aioboto3.Session
    session = Session()
    session: boto34.aioboto3.session.Session

    # Type annotated aioboto3.Client
    # Uses the same arguments as aioboto3.client method
    # Returns type annotated aioboto3 Organizations client
    organizations_client = session.organizations.client()
    organizations_client: types_aiobotocore_organizations.client.OrganizationsClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_organizations.client import OrganizationsClient
except ImportError:
    OrganizationsClient = object  # type: ignore[misc,assignment]


class OrganizationsService(
    ServiceFactory[OrganizationsClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "organizations"
    _SERVICE_PROP = "organizations"
