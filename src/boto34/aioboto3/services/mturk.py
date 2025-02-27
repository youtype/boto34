"""
Wrapper for aioboto3 MTurk service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_mturk/)

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
    # Returns type annotated aioboto3 MTurk client
    mturk_client = session.mturk.client()
    mturk_client: types_aiobotocore_mturk.client.MTurkClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_mturk.client import MTurkClient

from boto34.aioboto3.service_factory import ServiceFactory


class MTurkService(ServiceFactory[MTurkClient]):
    SERVICE_NAME = "mturk"
    _SERVICE_PROP = "mturk"
