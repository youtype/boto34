"""
Wrapper for boto3 Outposts service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_outposts/)

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
    # Returns type annotated boto3 Outposts client
    outposts_client = session.outposts.client()
    outposts_client: types_boto3_outposts.client.OutpostsClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_outposts.client import OutpostsClient
except ImportError:
    OutpostsClient = object  # type: ignore[misc,assignment]


class OutpostsService(
    ServiceFactory[OutpostsClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "outposts"
    _SERVICE_PROP = "outposts"
