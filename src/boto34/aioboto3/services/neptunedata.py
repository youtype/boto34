"""
Wrapper for aioboto3 NeptuneData service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_neptunedata/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_neptunedata.client import NeptuneDataClient

from boto34.aioboto3.service_factory import ServiceFactory


class NeptuneDataService(ServiceFactory[NeptuneDataClient]):
    """
    NeptuneData service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_neptunedata/)
    """
