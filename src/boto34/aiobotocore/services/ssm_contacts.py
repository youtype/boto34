"""
Wrapper for aiobotocore SSMContacts service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_contacts/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore SSMContacts client
    async with session.ssm_contacts.create_client() as ssm_contacts_client:
        ssm_contacts_client: types_aiobotocore_ssm_contacts.client.SSMContactsClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_ssm_contacts.client import SSMContactsClient

from boto34.aiobotocore.service_factory import ServiceFactory


class SSMContactsService(ServiceFactory[SSMContactsClient]):
    SERVICE_NAME = "ssm-contacts"
    _SERVICE_PROP = "ssm_contacts"
