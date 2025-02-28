"""
Wrapper for aiobotocore Neptune service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_neptune.client import NeptuneClient

from boto34.aiobotocore.service_factory import ServiceFactory


class NeptuneService(ServiceFactory[NeptuneClient]):
    """
    Neptune service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune/)
    """
