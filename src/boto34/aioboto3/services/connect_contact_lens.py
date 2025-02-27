"""
Wrapper for aioboto3 ConnectContactLens service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_connect_contact_lens/)

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
    # Returns type annotated aioboto3 ConnectContactLens client
    connect_contact_lens_client = session.connect_contact_lens.client()
    connect_contact_lens_client: types_aiobotocore_connect_contact_lens.client.ConnectContactLensClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_connect_contact_lens.client import ConnectContactLensClient

from boto34.aioboto3.service_factory import ServiceFactory


class ConnectContactLensService(ServiceFactory[ConnectContactLensClient]):
    SERVICE_NAME = "connect-contact-lens"
    _SERVICE_PROP = "connect_contact_lens"
