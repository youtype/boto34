"""
Wrapper for aiobotocore SageMakerMetrics service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker_metrics/)

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
    # Returns type annotated aiobotocore SageMakerMetrics client
    async with session.sagemaker_metrics.create_client() as sagemaker_metrics_client:
        sagemaker_metrics_client: types_aiobotocore_sagemaker_metrics.client.SageMakerMetricsClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_sagemaker_metrics.client import SageMakerMetricsClient

from boto34.aiobotocore.service_factory import ServiceFactory


class SageMakerMetricsService(ServiceFactory[SageMakerMetricsClient]):
    SERVICE_NAME = "sagemaker-metrics"
    _SERVICE_PROP = "sagemaker_metrics"
