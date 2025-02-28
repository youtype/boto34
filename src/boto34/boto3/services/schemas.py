"""
Wrapper for boto3 Schemas service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_schemas/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_schemas.client import SchemasClient

from boto34.boto3.service_factory import ServiceFactory


class SchemasService(ServiceFactory[SchemasClient]):
    """
    Schemas service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_schemas/)
    """
