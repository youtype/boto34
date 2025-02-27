"""
Wrapper for boto3 IoTTwinMaker service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_iottwinmaker/)

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
    # Returns type annotated boto3 IoTTwinMaker client
    iottwinmaker_client = session.iottwinmaker.client()
    iottwinmaker_client: types_boto3_iottwinmaker.client.IoTTwinMakerClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_iottwinmaker.client import IoTTwinMakerClient
except ImportError:
    IoTTwinMakerClient = object  # type: ignore[misc,assignment]


class IoTTwinMakerService(
    ServiceFactory[IoTTwinMakerClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "iottwinmaker"
    _SERVICE_PROP = "iottwinmaker"
