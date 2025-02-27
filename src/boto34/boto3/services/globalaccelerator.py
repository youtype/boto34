"""
Wrapper for boto3 GlobalAccelerator service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_globalaccelerator/)

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
    # Returns type annotated boto3 GlobalAccelerator client
    globalaccelerator_client = session.globalaccelerator.client()
    globalaccelerator_client: types_boto3_globalaccelerator.client.GlobalAcceleratorClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_globalaccelerator.client import GlobalAcceleratorClient
except ImportError:
    GlobalAcceleratorClient = object  # type: ignore[misc,assignment]


class GlobalAcceleratorService(
    ServiceFactory[GlobalAcceleratorClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "globalaccelerator"
    _SERVICE_PROP = "globalaccelerator"
