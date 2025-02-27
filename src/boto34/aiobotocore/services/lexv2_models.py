"""
Wrapper for aiobotocore LexModelsV2 service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore LexModelsV2 client
    async with session.lexv2_models.create_client() as lexv2_models_client:
        lexv2_models_client: types_aiobotocore_lexv2_models.client.LexModelsV2Client
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_lexv2_models.client import LexModelsV2Client
except ImportError:
    LexModelsV2Client = object  # type: ignore[misc,assignment]


class LexModelsV2Service(
    ServiceFactory[LexModelsV2Client]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "lexv2-models"
    _SERVICE_PROP = "lexv2_models"
