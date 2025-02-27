"""
Wrapper for boto3 Comprehend service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_comprehend/)

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
    # Returns type annotated boto3 Comprehend client
    comprehend_client = session.comprehend.client()
    comprehend_client: types_boto3_comprehend.client.ComprehendClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_comprehend.client import ComprehendClient
except ImportError:
    ComprehendClient = object  # type: ignore[misc,assignment]


class ComprehendService(
    ServiceFactory[ComprehendClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "comprehend"
    _SERVICE_PROP = "comprehend"
