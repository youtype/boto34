"""
Wrapper for boto3 CloudWatchObservabilityAdminService service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_observabilityadmin/)

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
    # Returns type annotated boto3 CloudWatchObservabilityAdminService client
    observabilityadmin_client = session.observabilityadmin.client()
    observabilityadmin_client: (
        types_boto3_observabilityadmin.client.CloudWatchObservabilityAdminServiceClient
    )
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_observabilityadmin.client import CloudWatchObservabilityAdminServiceClient
except ImportError:
    CloudWatchObservabilityAdminServiceClient = object  # type: ignore[misc,assignment]


class CloudWatchObservabilityAdminServiceService(
    ServiceFactory[CloudWatchObservabilityAdminServiceClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "observabilityadmin"
    _SERVICE_PROP = "observabilityadmin"
