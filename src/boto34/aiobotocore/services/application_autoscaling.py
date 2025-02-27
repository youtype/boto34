"""
Wrapper for aiobotocore ApplicationAutoScaling service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_application_autoscaling/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore ApplicationAutoScaling client
    async with session.application_autoscaling.create_client() as application_autoscaling_client:
        application_autoscaling_client: (
            types_aiobotocore_application_autoscaling.client.ApplicationAutoScalingClient
        )
    ```
"""

from __future__ import annotations

from types_aiobotocore_application_autoscaling.client import ApplicationAutoScalingClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_application_autoscaling.client import ApplicationAutoScalingClient
except ImportError:
    ApplicationAutoScalingClient = object  # type: ignore[misc,assignment]


class ApplicationAutoScalingService(
    ServiceFactory[ApplicationAutoScalingClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "application-autoscaling"
    _SERVICE_PROP = "application_autoscaling"
