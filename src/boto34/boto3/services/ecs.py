"""
Wrapper for boto3 ECS service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_ecs/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_ecs.client import ECSClient

from boto34.boto3.service_factory import ServiceFactory


class ECSService(ServiceFactory[ECSClient]):
    """
    ECS service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_ecs/)
    """
