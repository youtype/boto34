"""
Wrapper for aioboto3 AutoScaling service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_autoscaling/)

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
    # Returns type annotated aioboto3 AutoScaling client
    autoscaling_client = session.autoscaling.client()
    autoscaling_client: types_aiobotocore_autoscaling.client.AutoScalingClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_autoscaling.client import AutoScalingClient
except ImportError:
    AutoScalingClient = object  # type: ignore[misc,assignment]


class AutoScalingService(
    ServiceFactory[AutoScalingClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "autoscaling"
    _SERVICE_PROP = "autoscaling"
