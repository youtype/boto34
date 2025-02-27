"""
Wrapper for boto3 Macie2 service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_macie2/)

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
    # Returns type annotated boto3 Macie2 client
    macie2_client = session.macie2.client()
    macie2_client: types_boto3_macie2.client.Macie2Client
    ```
"""

from __future__ import annotations

from types_boto3_macie2.client import Macie2Client

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_macie2.client import Macie2Client
except ImportError:
    Macie2Client = object  # type: ignore[misc,assignment]


class Macie2Service(
    ServiceFactory[Macie2Client]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "macie2"
    _SERVICE_PROP = "macie2"
