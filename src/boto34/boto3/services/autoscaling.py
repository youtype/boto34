"""
Wrapper for boto3 AutoScaling service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_autoscaling/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_autoscaling.client import AutoScalingClient

from boto34.boto3.service_factory import ServiceFactory


class AutoScalingService(ServiceFactory[AutoScalingClient]):
    """
    AutoScaling service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_autoscaling/)
    """
