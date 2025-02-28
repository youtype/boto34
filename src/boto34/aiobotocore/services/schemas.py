"""
Wrapper for aiobotocore Schemas service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_schemas/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_schemas.client import SchemasClient

from boto34.aiobotocore.service_factory import ServiceFactory


class SchemasService(ServiceFactory[SchemasClient]):
    """
    Schemas service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_schemas/)
    """
