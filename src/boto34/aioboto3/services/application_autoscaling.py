"""
Wrapper for aioboto3 ApplicationAutoScaling service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_application_autoscaling/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_application_autoscaling.client import ApplicationAutoScalingClient

from boto34.aioboto3.service_factory import ServiceFactory


class ApplicationAutoScalingService(ServiceFactory[ApplicationAutoScalingClient]):
    """
    ApplicationAutoScaling service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_application_autoscaling/)
    """
