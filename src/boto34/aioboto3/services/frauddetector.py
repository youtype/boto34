"""
Wrapper for aioboto3 FraudDetector service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_frauddetector/)

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
    # Returns type annotated aioboto3 FraudDetector client
    frauddetector_client = session.frauddetector.client()
    frauddetector_client: types_aiobotocore_frauddetector.client.FraudDetectorClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_frauddetector.client import FraudDetectorClient
except ImportError:
    FraudDetectorClient = object  # type: ignore[misc,assignment]


class FraudDetectorService(
    ServiceFactory[FraudDetectorClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "frauddetector"
    _SERVICE_PROP = "frauddetector"
