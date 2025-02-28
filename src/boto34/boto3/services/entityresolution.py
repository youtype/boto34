"""
Wrapper for boto3 EntityResolution service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_entityresolution/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_entityresolution.client import EntityResolutionClient

from boto34.boto3.service_factory import ServiceFactory


class EntityResolutionService(ServiceFactory[EntityResolutionClient]):
    """
    EntityResolution service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_entityresolution/)
    """
