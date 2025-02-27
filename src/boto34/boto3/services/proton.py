"""
Wrapper for boto3 Proton service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_proton/)

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
    # Returns type annotated boto3 Proton client
    proton_client = session.proton.client()
    proton_client: types_boto3_proton.client.ProtonClient
    ```
"""

from __future__ import annotations

from types_boto3_proton.client import ProtonClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_proton.client import ProtonClient
except ImportError:
    ProtonClient = object  # type: ignore[misc,assignment]


class ProtonService(
    ServiceFactory[ProtonClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "proton"
    _SERVICE_PROP = "proton"
