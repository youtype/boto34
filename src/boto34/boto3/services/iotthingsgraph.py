"""
Wrapper for boto3 IoTThingsGraph service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_iotthingsgraph/)

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
    # Returns type annotated boto3 IoTThingsGraph client
    iotthingsgraph_client = session.iotthingsgraph.client()
    iotthingsgraph_client: types_boto3_iotthingsgraph.client.IoTThingsGraphClient
    ```
"""

from __future__ import annotations

from types_boto3_iotthingsgraph.client import IoTThingsGraphClient

from boto34.boto3.service_factory import ServiceFactory


class IoTThingsGraphService(ServiceFactory[IoTThingsGraphClient]):
    SERVICE_NAME = "iotthingsgraph"
    _SERVICE_PROP = "iotthingsgraph"
