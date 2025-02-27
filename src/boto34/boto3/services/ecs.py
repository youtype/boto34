"""
Wrapper for boto3 ECS service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_ecs/)

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
    # Returns type annotated boto3 ECS client
    ecs_client = session.ecs.client()
    ecs_client: types_boto3_ecs.client.ECSClient
    ```
"""

from __future__ import annotations

from types_boto3_ecs.client import ECSClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_ecs.client import ECSClient
except ImportError:
    ECSClient = object  # type: ignore[misc,assignment]


class ECSService(
    ServiceFactory[ECSClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "ecs"
    _SERVICE_PROP = "ecs"
