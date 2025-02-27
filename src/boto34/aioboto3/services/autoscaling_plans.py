"""
Wrapper for aioboto3 AutoScalingPlans service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_autoscaling_plans/)

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
    # Returns type annotated aioboto3 AutoScalingPlans client
    autoscaling_plans_client = session.autoscaling_plans.client()
    autoscaling_plans_client: types_aiobotocore_autoscaling_plans.client.AutoScalingPlansClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_autoscaling_plans.client import AutoScalingPlansClient
except ImportError:
    AutoScalingPlansClient = object  # type: ignore[misc,assignment]


class AutoScalingPlansService(
    ServiceFactory[AutoScalingPlansClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "autoscaling-plans"
    _SERVICE_PROP = "autoscaling_plans"
