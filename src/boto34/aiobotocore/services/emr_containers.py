"""
Wrapper for aiobotocore EMRContainers service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_emr_containers/)

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
    # Returns type annotated aiobotocore EMRContainers client
    async with session.emr_containers.create_client() as emr_containers_client:
        emr_containers_client: types_aiobotocore_emr_containers.client.EMRContainersClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_emr_containers.client import EMRContainersClient
except ImportError:
    EMRContainersClient = object  # type: ignore[misc,assignment]


class EMRContainersService(
    ServiceFactory[EMRContainersClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "emr-containers"
    _SERVICE_PROP = "emr_containers"
