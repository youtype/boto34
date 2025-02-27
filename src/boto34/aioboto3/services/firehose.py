"""
Wrapper for aioboto3 Firehose service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_firehose/)

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
    # Returns type annotated aioboto3 Firehose client
    firehose_client = session.firehose.client()
    firehose_client: types_aiobotocore_firehose.client.FirehoseClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_firehose.client import FirehoseClient
except ImportError:
    FirehoseClient = object  # type: ignore[misc,assignment]


class FirehoseService(
    ServiceFactory[FirehoseClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "firehose"
    _SERVICE_PROP = "firehose"
