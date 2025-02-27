"""
Wrapper for boto3 AmplifyBackend service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_amplifybackend/)

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
    # Returns type annotated boto3 AmplifyBackend client
    amplifybackend_client = session.amplifybackend.client()
    amplifybackend_client: types_boto3_amplifybackend.client.AmplifyBackendClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_amplifybackend.client import AmplifyBackendClient
except ImportError:
    AmplifyBackendClient = object  # type: ignore[misc,assignment]


class AmplifyBackendService(
    ServiceFactory[AmplifyBackendClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "amplifybackend"
    _SERVICE_PROP = "amplifybackend"
