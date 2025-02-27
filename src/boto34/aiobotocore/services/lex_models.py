"""
Wrapper for aiobotocore LexModelBuildingService service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lex_models/)

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
    # Returns type annotated aiobotocore LexModelBuildingService client
    async with session.lex_models.create_client() as lex_models_client:
        lex_models_client: types_aiobotocore_lex_models.client.LexModelBuildingServiceClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_lex_models.client import LexModelBuildingServiceClient
except ImportError:
    LexModelBuildingServiceClient = object  # type: ignore[misc,assignment]


class LexModelBuildingServiceService(
    ServiceFactory[LexModelBuildingServiceClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "lex-models"
    _SERVICE_PROP = "lex_models"
