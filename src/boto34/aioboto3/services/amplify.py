"""
Wrapper for aioboto3 Amplify service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_amplify/)

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
    # Returns type annotated aioboto3 Amplify client
    amplify_client = session.amplify.client()
    amplify_client: types_aiobotocore_amplify.client.AmplifyClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_amplify.client import AmplifyClient

from boto34.aioboto3.service_factory import ServiceFactory


class AmplifyService(ServiceFactory[AmplifyClient]):
    SERVICE_NAME = "amplify"
    _SERVICE_PROP = "amplify"
