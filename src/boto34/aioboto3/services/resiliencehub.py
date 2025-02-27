"""
Wrapper for aioboto3 ResilienceHub service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_resiliencehub/)

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
    # Returns type annotated aioboto3 ResilienceHub client
    resiliencehub_client = session.resiliencehub.client()
    resiliencehub_client: types_aiobotocore_resiliencehub.client.ResilienceHubClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_resiliencehub.client import ResilienceHubClient

from boto34.aioboto3.service_factory import ServiceFactory


class ResilienceHubService(ServiceFactory[ResilienceHubClient]):
    SERVICE_NAME = "resiliencehub"
    _SERVICE_PROP = "resiliencehub"
