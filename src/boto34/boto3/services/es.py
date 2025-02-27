"""
Wrapper for boto3 ElasticsearchService service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_es/)

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
    # Returns type annotated boto3 ElasticsearchService client
    es_client = session.es.client()
    es_client: types_boto3_es.client.ElasticsearchServiceClient
    ```
"""

from __future__ import annotations

from types_boto3_es.client import ElasticsearchServiceClient

from boto34.boto3.service_factory import ServiceFactory


class ElasticsearchServiceService(ServiceFactory[ElasticsearchServiceClient]):
    SERVICE_NAME = "es"
    _SERVICE_PROP = "es"
