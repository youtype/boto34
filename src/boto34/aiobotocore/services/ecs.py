"""
Wrapper for aiobotocore ECS service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ecs/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_ecs.client import ECSClient

from boto34.aiobotocore.service_factory import ServiceFactory


class ECSService(ServiceFactory[ECSClient]):
    """
    ECS service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ecs/)
    """
