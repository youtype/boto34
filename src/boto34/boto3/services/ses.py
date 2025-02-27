"""
Wrapper for boto3 SES service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_ses/)

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
    # Returns type annotated boto3 SES client
    ses_client = session.ses.client()
    ses_client: types_boto3_ses.client.SESClient
    ```
"""

from __future__ import annotations

from types_boto3_ses.client import SESClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_ses.client import SESClient
except ImportError:
    SESClient = object  # type: ignore[misc,assignment]


class SESService(
    ServiceFactory[SESClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "ses"
    _SERVICE_PROP = "ses"
