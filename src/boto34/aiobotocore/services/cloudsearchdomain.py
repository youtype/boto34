"""
Wrapper for aiobotocore CloudSearchDomain service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudsearchdomain/)

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
    # Returns type annotated aiobotocore CloudSearchDomain client
    async with session.cloudsearchdomain.create_client() as cloudsearchdomain_client:
        cloudsearchdomain_client: types_aiobotocore_cloudsearchdomain.client.CloudSearchDomainClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_cloudsearchdomain.client import CloudSearchDomainClient
except ImportError:
    CloudSearchDomainClient = object  # type: ignore[misc,assignment]


class CloudSearchDomainService(
    ServiceFactory[CloudSearchDomainClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "cloudsearchdomain"
    _SERVICE_PROP = "cloudsearchdomain"
