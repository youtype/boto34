"""
Wrapper for aioboto3 DirectoryServiceData service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_ds_data/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_ds_data.client import DirectoryServiceDataClient

from boto34.aioboto3.service_factory import ServiceFactory


class DirectoryServiceDataService(ServiceFactory[DirectoryServiceDataClient]):
    """
    DirectoryServiceData service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_ds_data/)
    """
