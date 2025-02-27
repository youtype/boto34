"""
Wrapper for boto3 AutoScaling service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_autoscaling/)

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
    # Returns type annotated boto3 AutoScaling client
    autoscaling_client = session.autoscaling.client()
    autoscaling_client: types_boto3_autoscaling.client.AutoScalingClient
    ```
"""

from __future__ import annotations

from types_boto3_autoscaling.client import AutoScalingClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_autoscaling.client import AutoScalingClient
except ImportError:
    AutoScalingClient = object  # type: ignore[misc,assignment]


class AutoScalingService(
    ServiceFactory[AutoScalingClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "autoscaling"
    _SERVICE_PROP = "autoscaling"
