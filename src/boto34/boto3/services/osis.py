"""
Wrapper for boto3 OpenSearchIngestion service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_osis/)

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
    # Returns type annotated boto3 OpenSearchIngestion client
    osis_client = session.osis.client()
    osis_client: types_boto3_osis.client.OpenSearchIngestionClient
    ```
"""

from __future__ import annotations

from types_boto3_osis.client import OpenSearchIngestionClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_osis.client import OpenSearchIngestionClient
except ImportError:
    OpenSearchIngestionClient = object  # type: ignore[misc,assignment]


class OpenSearchIngestionService(
    ServiceFactory[OpenSearchIngestionClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "osis"
    _SERVICE_PROP = "osis"
