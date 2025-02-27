"""
Wrapper for aiobotocore LocationService service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_location/)

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
    # Returns type annotated aiobotocore LocationService client
    async with session.location.create_client() as location_client:
        location_client: types_aiobotocore_location.client.LocationServiceClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_location.client import LocationServiceClient

from boto34.aiobotocore.service_factory import ServiceFactory


class LocationServiceService(ServiceFactory[LocationServiceClient]):
    SERVICE_NAME = "location"
    _SERVICE_PROP = "location"
