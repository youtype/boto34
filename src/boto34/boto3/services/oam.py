"""
Wrapper for boto3 CloudWatchObservabilityAccessManager service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_oam/)

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
    # Returns type annotated boto3 CloudWatchObservabilityAccessManager client
    oam_client = session.oam.client()
    oam_client: types_boto3_oam.client.CloudWatchObservabilityAccessManagerClient
    ```
"""

from __future__ import annotations

from types_boto3_oam.client import CloudWatchObservabilityAccessManagerClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_oam.client import CloudWatchObservabilityAccessManagerClient
except ImportError:
    CloudWatchObservabilityAccessManagerClient = object  # type: ignore[misc,assignment]


class CloudWatchObservabilityAccessManagerService(
    ServiceFactory[CloudWatchObservabilityAccessManagerClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "oam"
    _SERVICE_PROP = "oam"
