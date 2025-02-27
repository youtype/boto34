"""
Wrapper for aioboto3 DocDBElastic service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_docdb_elastic/)

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
    # Returns type annotated aioboto3 DocDBElastic client
    docdb_elastic_client = session.docdb_elastic.client()
    docdb_elastic_client: types_aiobotocore_docdb_elastic.client.DocDBElasticClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_docdb_elastic.client import DocDBElasticClient

from boto34.aioboto3.service_factory import ServiceFactory


class DocDBElasticService(ServiceFactory[DocDBElasticClient]):
    SERVICE_NAME = "docdb-elastic"
    _SERVICE_PROP = "docdb_elastic"
