"""
Wrapper for aioboto3 Signer service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_signer/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aioboto3 import Session

    # Wrapper for aioboto3.Session constructor
    # Returns boto34.Session inherited from aioboto3.Session
    session = Session()
    session: boto34.aioboto3.session.Session

    # Type annotated aioboto3.Client
    # Uses the same arguments as aioboto3.client method
    # Returns type annotated aioboto3 Signer client
    signer_client = session.signer.client()
    signer_client: types_aiobotocore_signer.client.SignerClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_signer.client import SignerClient

from boto34.aioboto3.service_factory import ServiceFactory


class SignerService(ServiceFactory[SignerClient]):
    SERVICE_NAME = "signer"
    _SERVICE_PROP = "signer"
