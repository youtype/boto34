"""
Wrapper for aiobotocore Signer service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_signer/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore Signer client
    async with session.signer.create_client() as signer_client:
        signer_client: types_aiobotocore_signer.client.SignerClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_signer.client import SignerClient
except ImportError:
    SignerClient = object  # type: ignore[misc,assignment]


class SignerService(
    ServiceFactory[SignerClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "signer"
    _SERVICE_PROP = "signer"
