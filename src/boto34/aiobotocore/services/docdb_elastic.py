"""
Wrapper for aiobotocore DocDBElastic service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_docdb_elastic/)

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
    # Returns type annotated aiobotocore DocDBElastic client
    async with session.docdb_elastic.create_client() as docdb_elastic_client:
        docdb_elastic_client: types_aiobotocore_docdb_elastic.client.DocDBElasticClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_docdb_elastic.client import DocDBElasticClient

from boto34.aiobotocore.service_factory import ServiceFactory


class DocDBElasticService(ServiceFactory[DocDBElasticClient]):
    SERVICE_NAME = "docdb-elastic"
    _SERVICE_PROP = "docdb_elastic"
