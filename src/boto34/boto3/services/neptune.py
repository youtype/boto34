"""
Wrapper for boto3 Neptune service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_neptune/)

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
    # Returns type annotated boto3 Neptune client
    neptune_client = session.neptune.client()
    neptune_client: types_boto3_neptune.client.NeptuneClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_neptune.client import NeptuneClient
except ImportError:
    NeptuneClient = object  # type: ignore[misc,assignment]


class NeptuneService(
    ServiceFactory[NeptuneClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "neptune"
    _SERVICE_PROP = "neptune"
