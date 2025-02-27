"""
Wrapper for boto3 Rekognition service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_rekognition/)

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
    # Returns type annotated boto3 Rekognition client
    rekognition_client = session.rekognition.client()
    rekognition_client: types_boto3_rekognition.client.RekognitionClient
    ```
"""

from __future__ import annotations

from types_boto3_rekognition.client import RekognitionClient

from boto34.boto3.service_factory import ServiceFactory


class RekognitionService(ServiceFactory[RekognitionClient]):
    SERVICE_NAME = "rekognition"
    _SERVICE_PROP = "rekognition"
