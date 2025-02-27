"""
Wrapper for aiobotocore ElasticInference service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_elastic_inference/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore ElasticInference client
    async with session.elastic_inference.create_client() as elastic_inference_client:
        elastic_inference_client: types_aiobotocore_elastic_inference.client.ElasticInferenceClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_elastic_inference.client import ElasticInferenceClient
except ImportError:
    ElasticInferenceClient = object  # type: ignore[misc,assignment]


class ElasticInferenceService(
    ServiceFactory[ElasticInferenceClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "elastic-inference"
    _SERVICE_PROP = "elastic_inference"
