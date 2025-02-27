"""
Wrapper for boto3 CloudHSMV2 service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cloudhsmv2/)

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
    # Returns type annotated boto3 CloudHSMV2 client
    cloudhsmv2_client = session.cloudhsmv2.client()
    cloudhsmv2_client: types_boto3_cloudhsmv2.client.CloudHSMV2Client
    ```
"""

from __future__ import annotations

from types_boto3_cloudhsmv2.client import CloudHSMV2Client

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_cloudhsmv2.client import CloudHSMV2Client
except ImportError:
    CloudHSMV2Client = object  # type: ignore[misc,assignment]


class CloudHSMV2Service(
    ServiceFactory[CloudHSMV2Client]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "cloudhsmv2"
    _SERVICE_PROP = "cloudhsmv2"
