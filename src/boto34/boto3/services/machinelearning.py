"""
Wrapper for boto3 MachineLearning service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_machinelearning/)

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
    # Returns type annotated boto3 MachineLearning client
    machinelearning_client = session.machinelearning.client()
    machinelearning_client: types_boto3_machinelearning.client.MachineLearningClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_machinelearning.client import MachineLearningClient
except ImportError:
    MachineLearningClient = object  # type: ignore[misc,assignment]


class MachineLearningService(
    ServiceFactory[MachineLearningClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "machinelearning"
    _SERVICE_PROP = "machinelearning"
