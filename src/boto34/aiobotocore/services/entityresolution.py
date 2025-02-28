"""
Wrapper for aiobotocore EntityResolution service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_entityresolution/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_entityresolution.client import EntityResolutionClient

from boto34.aiobotocore.service_factory import ServiceFactory


class EntityResolutionService(ServiceFactory[EntityResolutionClient]):
    """
    EntityResolution service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_entityresolution/)
    """
