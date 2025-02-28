"""
Wrapper for aioboto3 Neptune service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_neptune/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_neptune.client import NeptuneClient

from boto34.aioboto3.service_factory import ServiceFactory


class NeptuneService(ServiceFactory[NeptuneClient]):
    """
    Neptune service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_neptune/)
    """
