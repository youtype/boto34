"""
Wrapper for aioboto3 SSMContacts service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_ssm_contacts/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aioboto3 import Session

    # Wrapper for aioboto3.Session constructor
    # Returns boto34.Session inherited from aioboto3.Session
    session = Session()
    session: boto34.aioboto3.session.Session

    # Type annotated aioboto3.Client
    # Uses the same arguments as aioboto3.client method
    # Returns type annotated aioboto3 SSMContacts client
    ssm_contacts_client = session.ssm_contacts.client()
    ssm_contacts_client: types_aiobotocore_ssm_contacts.client.SSMContactsClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_ssm_contacts.client import SSMContactsClient
except ImportError:
    SSMContactsClient = object  # type: ignore[misc,assignment]


class SSMContactsService(
    ServiceFactory[SSMContactsClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "ssm-contacts"
    _SERVICE_PROP = "ssm_contacts"
