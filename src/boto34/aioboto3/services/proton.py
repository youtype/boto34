"""
Wrapper for aioboto3 Proton service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_proton/)

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
    # Returns type annotated aioboto3 Proton client
    proton_client = session.proton.client()
    proton_client: types_aiobotocore_proton.client.ProtonClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_proton.client import ProtonClient

from boto34.aioboto3.service_factory import ServiceFactory


class ProtonService(ServiceFactory[ProtonClient]):
    SERVICE_NAME = "proton"
    _SERVICE_PROP = "proton"
