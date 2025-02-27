"""
Wrapper for boto3 LexModelBuildingService service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_lex_models/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.boto3 import Session

    # Wrapper for boto3.Session constructor
    # Returns boto34.Session inherited from boto3.Session
    session = Session()
    session: boto34.boto3.session.Session

    # Type annotated boto3.Client
    # Uses the same arguments as boto3.client method
    # Returns type annotated boto3 LexModelBuildingService client
    lex_models_client = session.lex_models.client()
    lex_models_client: types_boto3_lex_models.client.LexModelBuildingServiceClient
    ```
"""

from __future__ import annotations

from types_boto3_lex_models.client import LexModelBuildingServiceClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_lex_models.client import LexModelBuildingServiceClient
except ImportError:
    LexModelBuildingServiceClient = object  # type: ignore[misc,assignment]


class LexModelBuildingServiceService(
    ServiceFactory[LexModelBuildingServiceClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "lex-models"
    _SERVICE_PROP = "lex_models"
