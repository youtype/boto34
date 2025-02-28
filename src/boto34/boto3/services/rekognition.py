"""
Wrapper for boto3 Rekognition service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_rekognition/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_rekognition.client import RekognitionClient

from boto34.boto3.service_factory import ServiceFactory


class RekognitionService(ServiceFactory[RekognitionClient]):
    """
    Rekognition service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_rekognition/)
    """
