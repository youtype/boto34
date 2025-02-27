"""
Wrapper for aioboto3 LexModelBuildingService service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_lex_models/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aioboto3 import Session

    # Wrapper for aioboto3.Session constructor
    # Returns boto34.Session inherited from aioboto3.Session
    session = Session()
    session: boto34.aioboto3.session.Session

    # Type annotated aioboto3.Client
    # Uses the same arguments as aioboto3.client method
    # Returns type annotated aioboto3 LexModelBuildingService client
    lex_models_client = session.lex_models.client()
    lex_models_client: types_aiobotocore_lex_models.client.LexModelBuildingServiceClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_lex_models.client import LexModelBuildingServiceClient

from boto34.aioboto3.service_factory import ServiceFactory


class LexModelBuildingServiceService(ServiceFactory[LexModelBuildingServiceClient]):
    SERVICE_NAME = "lex-models"
    _SERVICE_PROP = "lex_models"
