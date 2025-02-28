"""
Wrapper for aioboto3 FinSpaceData service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_finspace_data/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_finspace_data.client import FinSpaceDataClient

from boto34.aioboto3.service_factory import ServiceFactory


class FinSpaceDataService(ServiceFactory[FinSpaceDataClient]):
    """
    FinSpaceData service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_finspace_data/)
    """
