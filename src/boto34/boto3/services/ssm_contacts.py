"""
Wrapper for boto3 SSMContacts service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_ssm_contacts/)

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
    # Returns type annotated boto3 SSMContacts client
    ssm_contacts_client = session.ssm_contacts.client()
    ssm_contacts_client: types_boto3_ssm_contacts.client.SSMContactsClient
    ```
"""

from __future__ import annotations

from types_boto3_ssm_contacts.client import SSMContactsClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_ssm_contacts.client import SSMContactsClient
except ImportError:
    SSMContactsClient = object  # type: ignore[misc,assignment]


class SSMContactsService(
    ServiceFactory[SSMContactsClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "ssm-contacts"
    _SERVICE_PROP = "ssm_contacts"
