"""
Wrapper for boto3 ControlTower service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_controltower/)

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
    # Returns type annotated boto3 ControlTower client
    controltower_client = session.controltower.client()
    controltower_client: types_boto3_controltower.client.ControlTowerClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_controltower.client import ControlTowerClient
except ImportError:
    ControlTowerClient = object  # type: ignore[misc,assignment]


class ControlTowerService(
    ServiceFactory[ControlTowerClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "controltower"
    _SERVICE_PROP = "controltower"
