"""
Wrapper for boto3 ComputeOptimizer service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_compute_optimizer/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.boto3 import Session

    # Wrapper for boto3.Session constructor
    # Returns boto34.Session inherited from boto3.Session
    session = Session()
    session: boto34.boto3.session.Session

    # Type annotated boto3.Client
    # Uses the same arguments as boto3.client method
    # Returns type annotated boto3 ComputeOptimizer client
    compute_optimizer_client = session.compute_optimizer.client()
    compute_optimizer_client: types_boto3_compute_optimizer.client.ComputeOptimizerClient
    ```
"""

from __future__ import annotations

from types_boto3_compute_optimizer.client import ComputeOptimizerClient

from boto34.boto3.service_factory import ServiceFactory


class ComputeOptimizerService(ServiceFactory[ComputeOptimizerClient]):
    SERVICE_NAME = "compute-optimizer"
    _SERVICE_PROP = "compute_optimizer"
