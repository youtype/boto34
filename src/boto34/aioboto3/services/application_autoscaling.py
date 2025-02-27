"""
Wrapper for aioboto3 ApplicationAutoScaling service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_application_autoscaling/)

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
    # Returns type annotated aioboto3 ApplicationAutoScaling client
    application_autoscaling_client = session.application_autoscaling.client()
    application_autoscaling_client: (
        types_aiobotocore_application_autoscaling.client.ApplicationAutoScalingClient
    )
    ```
"""

from __future__ import annotations

from types_aiobotocore_application_autoscaling.client import ApplicationAutoScalingClient

from boto34.aioboto3.service_factory import ServiceFactory


class ApplicationAutoScalingService(ServiceFactory[ApplicationAutoScalingClient]):
    SERVICE_NAME = "application-autoscaling"
    _SERVICE_PROP = "application_autoscaling"
