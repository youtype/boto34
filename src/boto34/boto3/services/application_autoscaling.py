"""
Wrapper for boto3 ApplicationAutoScaling service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_application_autoscaling/)

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
    # Returns type annotated boto3 ApplicationAutoScaling client
    application_autoscaling_client = session.application_autoscaling.client()
    application_autoscaling_client: (
        types_boto3_application_autoscaling.client.ApplicationAutoScalingClient
    )
    ```
"""

from __future__ import annotations

from types_boto3_application_autoscaling.client import ApplicationAutoScalingClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_application_autoscaling.client import ApplicationAutoScalingClient
except ImportError:
    ApplicationAutoScalingClient = object  # type: ignore[misc,assignment]


class ApplicationAutoScalingService(
    ServiceFactory[ApplicationAutoScalingClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "application-autoscaling"
    _SERVICE_PROP = "application_autoscaling"
