"""
Wrapper for aioboto3 ComputeOptimizer service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_compute_optimizer/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aioboto3 import Session

    # Wrapper for aioboto3.Session constructor
    # Returns boto34.Session inherited from aioboto3.Session
    session = Session()
    session: boto34.aioboto3.session.Session

    # Type annotated aioboto3.Client
    # Uses the same arguments as aioboto3.client method
    # Returns type annotated aioboto3 ComputeOptimizer client
    compute_optimizer_client = session.compute_optimizer.client()
    compute_optimizer_client: types_aiobotocore_compute_optimizer.client.ComputeOptimizerClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_compute_optimizer.client import ComputeOptimizerClient
except ImportError:
    ComputeOptimizerClient = object  # type: ignore[misc,assignment]


class ComputeOptimizerService(
    ServiceFactory[ComputeOptimizerClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "compute-optimizer"
    _SERVICE_PROP = "compute_optimizer"
