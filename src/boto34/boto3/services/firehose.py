"""
Wrapper for boto3 Firehose service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_firehose/)

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
    # Returns type annotated boto3 Firehose client
    firehose_client = session.firehose.client()
    firehose_client: types_boto3_firehose.client.FirehoseClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_firehose.client import FirehoseClient
except ImportError:
    FirehoseClient = object  # type: ignore[misc,assignment]


class FirehoseService(
    ServiceFactory[FirehoseClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "firehose"
    _SERVICE_PROP = "firehose"
