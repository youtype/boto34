"""
Wrapper for aiobotocore CloudWatchObservabilityAdminService service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_observabilityadmin/)

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
    # Returns type annotated aiobotocore CloudWatchObservabilityAdminService client
    async with session.observabilityadmin.create_client() as observabilityadmin_client:
        observabilityadmin_client: (
            types_aiobotocore_observabilityadmin.client.CloudWatchObservabilityAdminServiceClient
        )
    ```
"""

from __future__ import annotations

from types_aiobotocore_observabilityadmin.client import CloudWatchObservabilityAdminServiceClient

from boto34.aiobotocore.service_factory import ServiceFactory


class CloudWatchObservabilityAdminServiceService(
    ServiceFactory[CloudWatchObservabilityAdminServiceClient]
):
    SERVICE_NAME = "observabilityadmin"
    _SERVICE_PROP = "observabilityadmin"
