"""
Wrapper for boto3 NeptuneData service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_neptunedata/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_neptunedata.client import NeptuneDataClient

from boto34.boto3.service_factory import ServiceFactory


class NeptuneDataService(ServiceFactory[NeptuneDataClient]):
    """
    NeptuneData service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_neptunedata/)
    """
