"""
Wrapper for aioboto3 AutoScalingPlans service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_autoscaling_plans/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_autoscaling_plans.client import AutoScalingPlansClient

from boto34.aioboto3.service_factory import ServiceFactory


class AutoScalingPlansService(ServiceFactory[AutoScalingPlansClient]):
    """
    AutoScalingPlans service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_autoscaling_plans/)
    """
