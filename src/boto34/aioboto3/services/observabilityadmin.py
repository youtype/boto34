"""
Wrapper for aioboto3 CloudWatchObservabilityAdminService service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_observabilityadmin/)

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
    # Returns type annotated aioboto3 CloudWatchObservabilityAdminService client
    observabilityadmin_client = session.observabilityadmin.client()
    observabilityadmin_client: (
        types_aiobotocore_observabilityadmin.client.CloudWatchObservabilityAdminServiceClient
    )
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_observabilityadmin.client import (
        CloudWatchObservabilityAdminServiceClient,
    )
except ImportError:
    CloudWatchObservabilityAdminServiceClient = object  # type: ignore[misc,assignment]


class CloudWatchObservabilityAdminServiceService(
    ServiceFactory[CloudWatchObservabilityAdminServiceClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "observabilityadmin"
    _SERVICE_PROP = "observabilityadmin"
