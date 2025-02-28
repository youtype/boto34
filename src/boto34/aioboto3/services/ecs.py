"""
Wrapper for aioboto3 ECS service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_ecs/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_ecs.client import ECSClient

from boto34.aioboto3.service_factory import ServiceFactory


class ECSService(ServiceFactory[ECSClient]):
    """
    ECS service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_ecs/)
    """
