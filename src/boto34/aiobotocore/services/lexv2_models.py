"""
Wrapper for aiobotocore LexModelsV2 service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_lexv2_models.client import LexModelsV2Client

from boto34.aiobotocore.service_factory import ServiceFactory


class LexModelsV2Service(ServiceFactory[LexModelsV2Client]):
    """
    LexModelsV2 service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/)
    """
