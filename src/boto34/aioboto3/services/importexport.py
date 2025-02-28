"""
Wrapper for aioboto3 ImportExport service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_importexport/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_importexport.client import ImportExportClient

from boto34.aioboto3.service_factory import ServiceFactory


class ImportExportService(ServiceFactory[ImportExportClient]):
    """
    ImportExport service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_importexport/)
    """
