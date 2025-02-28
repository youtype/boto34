"""
Wrapper for boto3 AutoScalingPlans service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_autoscaling_plans/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_autoscaling_plans.client import AutoScalingPlansClient

from boto34.boto3.service_factory import ServiceFactory


class AutoScalingPlansService(ServiceFactory[AutoScalingPlansClient]):
    """
    AutoScalingPlans service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_autoscaling_plans/)
    """
