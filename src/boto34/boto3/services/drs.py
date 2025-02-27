"""
Wrapper for boto3 Drs service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_drs/)

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
    # Returns type annotated boto3 Drs client
    drs_client = session.drs.client()
    drs_client: types_boto3_drs.client.DrsClient
    ```
"""

from __future__ import annotations

from types_boto3_drs.client import DrsClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_drs.client import DrsClient
except ImportError:
    DrsClient = object  # type: ignore[misc,assignment]


class DrsService(
    ServiceFactory[DrsClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "drs"
    _SERVICE_PROP = "drs"
