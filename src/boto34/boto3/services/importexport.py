"""
Wrapper for boto3 ImportExport service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_importexport/)

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
    # Returns type annotated boto3 ImportExport client
    importexport_client = session.importexport.client()
    importexport_client: types_boto3_importexport.client.ImportExportClient
    ```
"""

from __future__ import annotations

from types_boto3_importexport.client import ImportExportClient

from boto34.boto3.service_factory import ServiceFactory


class ImportExportService(ServiceFactory[ImportExportClient]):
    SERVICE_NAME = "importexport"
    _SERVICE_PROP = "importexport"
