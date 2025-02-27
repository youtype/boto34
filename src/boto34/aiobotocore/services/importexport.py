"""
Wrapper for aiobotocore ImportExport service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_importexport/)

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
    # Returns type annotated aiobotocore ImportExport client
    async with session.importexport.create_client() as importexport_client:
        importexport_client: types_aiobotocore_importexport.client.ImportExportClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_importexport.client import ImportExportClient

from boto34.aiobotocore.service_factory import ServiceFactory


class ImportExportService(ServiceFactory[ImportExportClient]):
    SERVICE_NAME = "importexport"
    _SERVICE_PROP = "importexport"
