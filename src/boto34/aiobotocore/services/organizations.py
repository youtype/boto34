"""
Wrapper for aiobotocore Organizations service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_organizations/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore Organizations client
    async with session.organizations.create_client() as organizations_client:
        organizations_client: types_aiobotocore_organizations.client.OrganizationsClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_organizations.client import OrganizationsClient

from boto34.aiobotocore.service_factory import ServiceFactory


class OrganizationsService(ServiceFactory[OrganizationsClient]):
    SERVICE_NAME = "organizations"
    _SERVICE_PROP = "organizations"
