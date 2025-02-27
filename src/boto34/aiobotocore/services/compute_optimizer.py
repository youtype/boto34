"""
Wrapper for aiobotocore ComputeOptimizer service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_compute_optimizer/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore ComputeOptimizer client
    async with session.compute_optimizer.create_client() as compute_optimizer_client:
        compute_optimizer_client: types_aiobotocore_compute_optimizer.client.ComputeOptimizerClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_compute_optimizer.client import ComputeOptimizerClient

from boto34.aiobotocore.service_factory import ServiceFactory


class ComputeOptimizerService(ServiceFactory[ComputeOptimizerClient]):
    SERVICE_NAME = "compute-optimizer"
    _SERVICE_PROP = "compute_optimizer"
