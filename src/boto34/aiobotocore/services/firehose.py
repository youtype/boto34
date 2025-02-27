"""
Wrapper for aiobotocore Firehose service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_firehose/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore Firehose client
    async with session.firehose.create_client() as firehose_client:
        firehose_client: types_aiobotocore_firehose.client.FirehoseClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_firehose.client import FirehoseClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_firehose.client import FirehoseClient
except ImportError:
    FirehoseClient = object  # type: ignore[misc,assignment]


class FirehoseService(
    ServiceFactory[FirehoseClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "firehose"
    _SERVICE_PROP = "firehose"
