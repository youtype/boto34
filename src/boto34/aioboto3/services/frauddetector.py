"""
Wrapper for aioboto3 FraudDetector service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_frauddetector/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_frauddetector.client import FraudDetectorClient

from boto34.aioboto3.service_factory import ServiceFactory


class FraudDetectorService(ServiceFactory[FraudDetectorClient]):
    """
    FraudDetector service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_frauddetector/)
    """
