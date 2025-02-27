"""
Wrapper for boto3 FreeTier service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_freetier/)

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
    # Returns type annotated boto3 FreeTier client
    freetier_client = session.freetier.client()
    freetier_client: types_boto3_freetier.client.FreeTierClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_freetier.client import FreeTierClient
except ImportError:
    FreeTierClient = object  # type: ignore[misc,assignment]


class FreeTierService(
    ServiceFactory[FreeTierClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "freetier"
    _SERVICE_PROP = "freetier"
