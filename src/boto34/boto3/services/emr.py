"""
Wrapper for boto3 EMR service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_emr/)

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
    # Returns type annotated boto3 EMR client
    emr_client = session.emr.client()
    emr_client: types_boto3_emr.client.EMRClient
    ```
"""

from __future__ import annotations

from types_boto3_emr.client import EMRClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_emr.client import EMRClient
except ImportError:
    EMRClient = object  # type: ignore[misc,assignment]


class EMRService(
    ServiceFactory[EMRClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "emr"
    _SERVICE_PROP = "emr"
