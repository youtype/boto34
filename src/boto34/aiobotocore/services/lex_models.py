"""
Wrapper for aiobotocore LexModelBuildingService service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lex_models/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_lex_models.client import LexModelBuildingServiceClient

from boto34.aiobotocore.service_factory import ServiceFactory


class LexModelBuildingServiceService(ServiceFactory[LexModelBuildingServiceClient]):
    """
    LexModelBuildingService service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lex_models/)
    """
