"""
Wrapper for boto3 MTurk service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_mturk/)

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
    # Returns type annotated boto3 MTurk client
    mturk_client = session.mturk.client()
    mturk_client: types_boto3_mturk.client.MTurkClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_mturk.client import MTurkClient
except ImportError:
    MTurkClient = object  # type: ignore[misc,assignment]


class MTurkService(
    ServiceFactory[MTurkClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "mturk"
    _SERVICE_PROP = "mturk"
