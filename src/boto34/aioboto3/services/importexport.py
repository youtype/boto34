"""
Wrapper for aioboto3 ImportExport service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_importexport/)

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
    # Returns type annotated aioboto3 ImportExport client
    importexport_client = session.importexport.client()
    importexport_client: types_aiobotocore_importexport.client.ImportExportClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_importexport.client import ImportExportClient

from boto34.aioboto3.service_factory import ServiceFactory


class ImportExportService(ServiceFactory[ImportExportClient]):
    SERVICE_NAME = "importexport"
    _SERVICE_PROP = "importexport"
