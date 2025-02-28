"""
Wrapper for aioboto3 EntityResolution service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_entityresolution/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_entityresolution.client import EntityResolutionClient

from boto34.aioboto3.service_factory import ServiceFactory


class EntityResolutionService(ServiceFactory[EntityResolutionClient]):
    """
    EntityResolution service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_entityresolution/)
    """
