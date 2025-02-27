"""
Wrapper for aiobotocore AutoScaling service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_autoscaling/)

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
    # Returns type annotated aiobotocore AutoScaling client
    async with session.autoscaling.create_client() as autoscaling_client:
        autoscaling_client: types_aiobotocore_autoscaling.client.AutoScalingClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_autoscaling.client import AutoScalingClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_autoscaling.client import AutoScalingClient
except ImportError:
    AutoScalingClient = object  # type: ignore[misc,assignment]


class AutoScalingService(
    ServiceFactory[AutoScalingClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "autoscaling"
    _SERVICE_PROP = "autoscaling"
