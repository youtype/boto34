"""
Wrapper for boto3 Amplify service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_amplify/)

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
    # Returns type annotated boto3 Amplify client
    amplify_client = session.amplify.client()
    amplify_client: types_boto3_amplify.client.AmplifyClient
    ```
"""

from __future__ import annotations

from types_boto3_amplify.client import AmplifyClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_amplify.client import AmplifyClient
except ImportError:
    AmplifyClient = object  # type: ignore[misc,assignment]


class AmplifyService(
    ServiceFactory[AmplifyClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "amplify"
    _SERVICE_PROP = "amplify"
