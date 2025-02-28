"""
Wrapper for aiobotocore NeptuneGraph service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_neptune_graph.client import NeptuneGraphClient

from boto34.aiobotocore.service_factory import ServiceFactory


class NeptuneGraphService(ServiceFactory[NeptuneGraphClient]):
    """
    NeptuneGraph service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/)
    """
