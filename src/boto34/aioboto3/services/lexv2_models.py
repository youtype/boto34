"""
Wrapper for aioboto3 LexModelsV2 service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_lexv2_models/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_lexv2_models.client import LexModelsV2Client

from boto34.aioboto3.service_factory import ServiceFactory


class LexModelsV2Service(ServiceFactory[LexModelsV2Client]):
    """
    LexModelsV2 service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_lexv2_models/)
    """
