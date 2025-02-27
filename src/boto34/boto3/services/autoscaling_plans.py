"""
Wrapper for boto3 AutoScalingPlans service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_autoscaling_plans/)

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
    # Returns type annotated boto3 AutoScalingPlans client
    autoscaling_plans_client = session.autoscaling_plans.client()
    autoscaling_plans_client: types_boto3_autoscaling_plans.client.AutoScalingPlansClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_autoscaling_plans.client import AutoScalingPlansClient
except ImportError:
    AutoScalingPlansClient = object  # type: ignore[misc,assignment]


class AutoScalingPlansService(
    ServiceFactory[AutoScalingPlansClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "autoscaling-plans"
    _SERVICE_PROP = "autoscaling_plans"
