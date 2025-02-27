"""
Wrapper for aioboto3 Polly service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_polly/)

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
    # Returns type annotated aioboto3 Polly client
    polly_client = session.polly.client()
    polly_client: types_aiobotocore_polly.client.PollyClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_polly.client import PollyClient

from boto34.aioboto3.service_factory import ServiceFactory


class PollyService(ServiceFactory[PollyClient]):
    SERVICE_NAME = "polly"
    _SERVICE_PROP = "polly"
