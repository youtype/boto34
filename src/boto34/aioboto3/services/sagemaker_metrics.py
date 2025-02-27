"""
Wrapper for aioboto3 SageMakerMetrics service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_sagemaker_metrics/)

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
    # Returns type annotated aioboto3 SageMakerMetrics client
    sagemaker_metrics_client = session.sagemaker_metrics.client()
    sagemaker_metrics_client: types_aiobotocore_sagemaker_metrics.client.SageMakerMetricsClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_sagemaker_metrics.client import SageMakerMetricsClient
except ImportError:
    SageMakerMetricsClient = object  # type: ignore[misc,assignment]


class SageMakerMetricsService(
    ServiceFactory[SageMakerMetricsClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "sagemaker-metrics"
    _SERVICE_PROP = "sagemaker_metrics"
