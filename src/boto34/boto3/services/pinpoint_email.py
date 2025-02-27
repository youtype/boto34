"""
Wrapper for boto3 PinpointEmail service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_pinpoint_email/)

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
    # Returns type annotated boto3 PinpointEmail client
    pinpoint_email_client = session.pinpoint_email.client()
    pinpoint_email_client: types_boto3_pinpoint_email.client.PinpointEmailClient
    ```
"""

from __future__ import annotations

from types_boto3_pinpoint_email.client import PinpointEmailClient

from boto34.boto3.service_factory import ServiceFactory


class PinpointEmailService(ServiceFactory[PinpointEmailClient]):
    SERVICE_NAME = "pinpoint-email"
    _SERVICE_PROP = "pinpoint_email"
