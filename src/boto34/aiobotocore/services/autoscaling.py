"""
Wrapper for aiobotocore AutoScaling service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_autoscaling/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_autoscaling.client import AutoScalingClient

from boto34.aiobotocore.service_factory import ServiceFactory


class AutoScalingService(ServiceFactory[AutoScalingClient]):
    """
    AutoScaling service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_autoscaling/)
    """
