"""
Wrapper for boto3 Redshift service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_redshift/)

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
    # Returns type annotated boto3 Redshift client
    redshift_client = session.redshift.client()
    redshift_client: types_boto3_redshift.client.RedshiftClient
    ```
"""

from __future__ import annotations

from types_boto3_redshift.client import RedshiftClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_redshift.client import RedshiftClient
except ImportError:
    RedshiftClient = object  # type: ignore[misc,assignment]


class RedshiftService(
    ServiceFactory[RedshiftClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "redshift"
    _SERVICE_PROP = "redshift"
