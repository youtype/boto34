"""
Wrapper for boto3 ImportExport service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_importexport/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_importexport.client import ImportExportClient

from boto34.boto3.service_factory import ServiceFactory


class ImportExportService(ServiceFactory[ImportExportClient]):
    """
    ImportExport service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_importexport/)
    """
