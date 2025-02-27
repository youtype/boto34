"""
Wrapper for boto3 IoTFleetWise service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_iotfleetwise/)

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
    # Returns type annotated boto3 IoTFleetWise client
    iotfleetwise_client = session.iotfleetwise.client()
    iotfleetwise_client: types_boto3_iotfleetwise.client.IoTFleetWiseClient
    ```
"""

from __future__ import annotations

from types_boto3_iotfleetwise.client import IoTFleetWiseClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_iotfleetwise.client import IoTFleetWiseClient
except ImportError:
    IoTFleetWiseClient = object  # type: ignore[misc,assignment]


class IoTFleetWiseService(
    ServiceFactory[IoTFleetWiseClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "iotfleetwise"
    _SERVICE_PROP = "iotfleetwise"
