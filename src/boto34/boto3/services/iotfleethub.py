"""
Wrapper for boto3 IoTFleetHub service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_iotfleethub/)

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
    # Returns type annotated boto3 IoTFleetHub client
    iotfleethub_client = session.iotfleethub.client()
    iotfleethub_client: types_boto3_iotfleethub.client.IoTFleetHubClient
    ```
"""

from __future__ import annotations

from types_boto3_iotfleethub.client import IoTFleetHubClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_iotfleethub.client import IoTFleetHubClient
except ImportError:
    IoTFleetHubClient = object  # type: ignore[misc,assignment]


class IoTFleetHubService(
    ServiceFactory[IoTFleetHubClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "iotfleethub"
    _SERVICE_PROP = "iotfleethub"
