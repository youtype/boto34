"""
Wrapper for boto3 AmplifyUIBuilder service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_amplifyuibuilder/)

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
    # Returns type annotated boto3 AmplifyUIBuilder client
    amplifyuibuilder_client = session.amplifyuibuilder.client()
    amplifyuibuilder_client: types_boto3_amplifyuibuilder.client.AmplifyUIBuilderClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_amplifyuibuilder.client import AmplifyUIBuilderClient
except ImportError:
    AmplifyUIBuilderClient = object  # type: ignore[misc,assignment]


class AmplifyUIBuilderService(
    ServiceFactory[AmplifyUIBuilderClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "amplifyuibuilder"
    _SERVICE_PROP = "amplifyuibuilder"
