"""
Wrapper for boto3 AccessAnalyzer service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_accessanalyzer/)

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
    # Returns type annotated boto3 AccessAnalyzer client
    accessanalyzer_client = session.accessanalyzer.client()
    accessanalyzer_client: types_boto3_accessanalyzer.client.AccessAnalyzerClient
    ```
"""

from __future__ import annotations

from types_boto3_accessanalyzer.client import AccessAnalyzerClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_accessanalyzer.client import AccessAnalyzerClient
except ImportError:
    AccessAnalyzerClient = object  # type: ignore[misc,assignment]


class AccessAnalyzerService(
    ServiceFactory[AccessAnalyzerClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "accessanalyzer"
    _SERVICE_PROP = "accessanalyzer"
