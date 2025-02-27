"""
Wrapper for aioboto3 MachineLearning service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_machinelearning/)

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
    # Returns type annotated aioboto3 MachineLearning client
    machinelearning_client = session.machinelearning.client()
    machinelearning_client: types_aiobotocore_machinelearning.client.MachineLearningClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_machinelearning.client import MachineLearningClient
except ImportError:
    MachineLearningClient = object  # type: ignore[misc,assignment]


class MachineLearningService(
    ServiceFactory[MachineLearningClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "machinelearning"
    _SERVICE_PROP = "machinelearning"
