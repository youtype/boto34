"""
Wrapper for boto3 Signer service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_signer/)

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
    # Returns type annotated boto3 Signer client
    signer_client = session.signer.client()
    signer_client: types_boto3_signer.client.SignerClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_signer.client import SignerClient
except ImportError:
    SignerClient = object  # type: ignore[misc,assignment]


class SignerService(
    ServiceFactory[SignerClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "signer"
    _SERVICE_PROP = "signer"
