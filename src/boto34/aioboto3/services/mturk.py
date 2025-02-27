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

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_mturk.client import MTurkClient
except ImportError:
    MTurkClient = object  # type: ignore[misc,assignment]


class MTurkService(
    ServiceFactory[MTurkClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "mturk"
    _SERVICE_PROP = "mturk"
