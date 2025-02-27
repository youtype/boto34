"""
Wrapper for aiobotocore AutoScalingPlans service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_autoscaling_plans/)

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
    # Returns type annotated aiobotocore AutoScalingPlans client
    async with session.autoscaling_plans.create_client() as autoscaling_plans_client:
        autoscaling_plans_client: types_aiobotocore_autoscaling_plans.client.AutoScalingPlansClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_autoscaling_plans.client import AutoScalingPlansClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_autoscaling_plans.client import AutoScalingPlansClient
except ImportError:
    AutoScalingPlansClient = object  # type: ignore[misc,assignment]


class AutoScalingPlansService(
    ServiceFactory[AutoScalingPlansClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "autoscaling-plans"
    _SERVICE_PROP = "autoscaling_plans"
