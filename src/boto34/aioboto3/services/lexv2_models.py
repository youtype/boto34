"""
Wrapper for aioboto3 LexModelsV2 service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_lexv2_models/)

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
    # Returns type annotated aioboto3 LexModelsV2 client
    lexv2_models_client = session.lexv2_models.client()
    lexv2_models_client: types_aiobotocore_lexv2_models.client.LexModelsV2Client
    ```
"""

from __future__ import annotations

from types_aiobotocore_lexv2_models.client import LexModelsV2Client

from boto34.aioboto3.service_factory import ServiceFactory


class LexModelsV2Service(ServiceFactory[LexModelsV2Client]):
    SERVICE_NAME = "lexv2-models"
    _SERVICE_PROP = "lexv2_models"
