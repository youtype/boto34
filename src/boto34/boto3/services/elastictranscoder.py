"""
Wrapper for boto3 ElasticTranscoder service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_elastictranscoder/)

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
    # Returns type annotated boto3 ElasticTranscoder client
    elastictranscoder_client = session.elastictranscoder.client()
    elastictranscoder_client: types_boto3_elastictranscoder.client.ElasticTranscoderClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_elastictranscoder.client import ElasticTranscoderClient
except ImportError:
    ElasticTranscoderClient = object  # type: ignore[misc,assignment]


class ElasticTranscoderService(
    ServiceFactory[ElasticTranscoderClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "elastictranscoder"
    _SERVICE_PROP = "elastictranscoder"
