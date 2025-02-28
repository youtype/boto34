"""
Wrapper for boto3 DirectoryServiceData service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_ds_data/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_ds_data.client import DirectoryServiceDataClient

from boto34.boto3.service_factory import ServiceFactory


class DirectoryServiceDataService(ServiceFactory[DirectoryServiceDataClient]):
    """
    DirectoryServiceData service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_ds_data/)
    """
