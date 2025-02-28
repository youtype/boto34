"""
Wrapper for aioboto3 Glue service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_glue/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_glue.client import GlueClient

from boto34.aioboto3.service_factory import ServiceFactory


class GlueService(ServiceFactory[GlueClient]):
    """
    Glue service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_glue/)
    """
