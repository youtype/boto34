"""
Wrapper for boto3 DocDBElastic service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_docdb_elastic/)

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
    # Returns type annotated boto3 DocDBElastic client
    docdb_elastic_client = session.docdb_elastic.client()
    docdb_elastic_client: types_boto3_docdb_elastic.client.DocDBElasticClient
    ```
"""

from __future__ import annotations

from types_boto3_docdb_elastic.client import DocDBElasticClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_docdb_elastic.client import DocDBElasticClient
except ImportError:
    DocDBElasticClient = object  # type: ignore[misc,assignment]


class DocDBElasticService(
    ServiceFactory[DocDBElasticClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "docdb-elastic"
    _SERVICE_PROP = "docdb_elastic"
