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

from types_boto3_mturk.client import MTurkClient

from boto34.boto3.service_factory import ServiceFactory


class MTurkService(ServiceFactory[MTurkClient]):
    SERVICE_NAME = "mturk"
    _SERVICE_PROP = "mturk"
