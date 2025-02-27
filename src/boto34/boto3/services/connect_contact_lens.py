"""
Wrapper for boto3 ConnectContactLens service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_connect_contact_lens/)

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
    # Returns type annotated boto3 ConnectContactLens client
    connect_contact_lens_client = session.connect_contact_lens.client()
    connect_contact_lens_client: types_boto3_connect_contact_lens.client.ConnectContactLensClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_connect_contact_lens.client import ConnectContactLensClient
except ImportError:
    ConnectContactLensClient = object  # type: ignore[misc,assignment]


class ConnectContactLensService(
    ServiceFactory[ConnectContactLensClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "connect-contact-lens"
    _SERVICE_PROP = "connect_contact_lens"
