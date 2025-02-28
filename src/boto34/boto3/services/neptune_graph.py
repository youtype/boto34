"""
Wrapper for boto3 NeptuneGraph service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_neptune_graph/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_neptune_graph.client import NeptuneGraphClient

from boto34.boto3.service_factory import ServiceFactory


class NeptuneGraphService(ServiceFactory[NeptuneGraphClient]):
    """
    NeptuneGraph service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_neptune_graph/)
    """
