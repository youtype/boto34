"""
Wrapper for aiobotocore Rekognition service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_rekognition.client import RekognitionClient

from boto34.aiobotocore.service_factory import ServiceFactory


class RekognitionService(ServiceFactory[RekognitionClient]):
    """
    Rekognition service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/)
    """
