"""
Wrapper for boto3 FraudDetector service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_frauddetector/)

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
    # Returns type annotated boto3 FraudDetector client
    frauddetector_client = session.frauddetector.client()
    frauddetector_client: types_boto3_frauddetector.client.FraudDetectorClient
    ```
"""

from __future__ import annotations

from types_boto3_frauddetector.client import FraudDetectorClient

from boto34.boto3.service_factory import ServiceFactory


class FraudDetectorService(ServiceFactory[FraudDetectorClient]):
    SERVICE_NAME = "frauddetector"
    _SERVICE_PROP = "frauddetector"
