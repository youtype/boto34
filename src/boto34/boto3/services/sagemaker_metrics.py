"""
Wrapper for boto3 SageMakerMetrics service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_sagemaker_metrics/)

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
    # Returns type annotated boto3 SageMakerMetrics client
    sagemaker_metrics_client = session.sagemaker_metrics.client()
    sagemaker_metrics_client: types_boto3_sagemaker_metrics.client.SageMakerMetricsClient
    ```
"""

from __future__ import annotations

from types_boto3_sagemaker_metrics.client import SageMakerMetricsClient

from boto34.boto3.service_factory import ServiceFactory


class SageMakerMetricsService(ServiceFactory[SageMakerMetricsClient]):
    SERVICE_NAME = "sagemaker-metrics"
    _SERVICE_PROP = "sagemaker_metrics"
