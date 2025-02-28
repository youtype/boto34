"""
Wrapper for aioboto3 ComputeOptimizer service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_compute_optimizer/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_compute_optimizer.client import ComputeOptimizerClient

from boto34.aioboto3.service_factory import ServiceFactory


class ComputeOptimizerService(ServiceFactory[ComputeOptimizerClient]):
    """
    ComputeOptimizer service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_compute_optimizer/)
    """
