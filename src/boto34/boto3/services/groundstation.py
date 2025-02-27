"""
Wrapper for boto3 GroundStation service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_groundstation/)

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
    # Returns type annotated boto3 GroundStation client
    groundstation_client = session.groundstation.client()
    groundstation_client: types_boto3_groundstation.client.GroundStationClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_groundstation.client import GroundStationClient
except ImportError:
    GroundStationClient = object  # type: ignore[misc,assignment]


class GroundStationService(
    ServiceFactory[GroundStationClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "groundstation"
    _SERVICE_PROP = "groundstation"
