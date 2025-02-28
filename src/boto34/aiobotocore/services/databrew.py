"""
Wrapper for aiobotocore GlueDataBrew service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_databrew/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_databrew.client import GlueDataBrewClient

from boto34.aiobotocore.service_factory import ServiceFactory


class GlueDataBrewService(ServiceFactory[GlueDataBrewClient]):
    """
    GlueDataBrew service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_databrew/)
    """
