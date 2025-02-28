"""
Wrapper for aiobotocore DirectoryServiceData service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ds_data/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_ds_data.client import DirectoryServiceDataClient

from boto34.aiobotocore.service_factory import ServiceFactory


class DirectoryServiceDataService(ServiceFactory[DirectoryServiceDataClient]):
    """
    DirectoryServiceData service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ds_data/)
    """
