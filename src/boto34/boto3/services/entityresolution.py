"""
Wrapper for boto3 EntityResolution service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_entityresolution/)

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
    # Returns type annotated boto3 EntityResolution client
    entityresolution_client = session.entityresolution.client()
    entityresolution_client: types_boto3_entityresolution.client.EntityResolutionClient
    ```
"""

from __future__ import annotations

from types_boto3_entityresolution.client import EntityResolutionClient

from boto34.boto3.service_factory import ServiceFactory


class EntityResolutionService(ServiceFactory[EntityResolutionClient]):
    SERVICE_NAME = "entityresolution"
    _SERVICE_PROP = "entityresolution"
